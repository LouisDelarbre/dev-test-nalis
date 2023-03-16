from odoo import api, fields, models, Command
from datetime import datetime
import base64
import xlrd

class AdaptorResume(models.Model):

    _name = "adaptor.resume"
    _description = "adaptation's resume for prices or other field from POS"

    wal_product_modif_ids = fields.One2many("adaptor.product", "wal_adaptor_resume_id",string="products", readonly=True, auto_join=True)
    wal_date_modif = fields.Date(string='Modification date', default=datetime.today(), readonly=True)
    wal_customize_import = fields.Boolean(string="Customise the import")
    wal_xls_file = fields.Binary('Excel file to import')
    wal_import_properties_ids = fields.One2many("adaptor.import.property", "wal_adaptor_resume_id",string="Property", auto_join=True)
    wal_selection_reference_field = fields.Selection(string="Reference Field Selection",selection=lambda self: self.dynamic_selection_fields() )
    wal_col_excel_reference = fields.Integer("number of the column to import : a =1, b=2, etc...")


    #check and return all the available fields for product.template
    def dynamic_selection_fields(self):
        
        # get all the fields for product.template
        ## ? is it the good way to do it ? 
        select_dict = self.env['product.template']._fields
        select_list = []
        for key, val in select_dict.items():
            select_list.append((key, key))

        return select_list

    #create resume adaptation and add list of product who need to change the price
    @api.model
    def create(self, vals):

        res = super(AdaptorResume, self).create(vals)
        ## ? is it better to use res.value or vals["value"] ?

        product_array = []

        wb = xlrd.open_workbook(file_contents=base64.b64decode(vals["wal_xls_file"]), formatting_info = True)

        # check in excel file if there is barcode correspondance
        for sheet in wb.sheets():
            # if user want to customize import
            if vals["wal_customize_import"]:
                idx = 0
                for cell in sheet.col(vals["wal_col_excel_reference"]-1):
                    if cell.ctype == 1:
                        str_cell_value = cell.value
                    elif cell.ctype == 2:
                        str_cell_value = str(int(cell.value))
                    else :
                        str_cell_value = str(cell.value)
                    prod_test = self.env['product.template'].search([(vals["wal_selection_reference_field"],'=',str_cell_value)])
                    for product in prod_test:
                        if product :

                            for property in res.import_properties_ids:
                                idx_cell = property.col_excel_import -1
                                if getattr(product, property.field_related_to_col) != sheet.cell_value(idx,idx_cell):
                                    product_array.append( Command.create({
                                                            "wal_product_id": product.id,
                                                            "wal_field_type": property.field_related_to_col,
                                                            "wal_old": getattr(product, property.field_related_to_col),
                                                            "wal_new": sheet.cell_value(idx,idx_cell)
                                    })) 
                                    # adapt attribute
                                    setattr(product, property.field_related_to_col, sheet.cell_value(idx,idx_cell))   
                             
                    idx += 1 

            else : 
                # if user want to use the classic settings who change the standard price ( cost) and list_price(price)
                idx = 0
                for ean in sheet.col(0):
                    if ean.ctype == 2:
                        str_ean_value = str(int(ean.value))
                        prod_test = self.env['product.template'].search([('barcode','=',str_ean_value)])
                        for product in prod_test:
                            if product : 
                                if product.list_price != sheet.cell_value(idx,6):
                                    product_array.append( Command.create({
                                                                "wal_product_id": product.id,
                                                                "wal_field_type": "list_price",
                                                                "wal_old": product.list_price,
                                                                "wal_new": sheet.cell_value(idx,6)
                                    }))
                                    product_array.append( Command.create({
                                                                "wal_product_id": product.id,
                                                                "wal_field_type": "standard_price",
                                                                "wal_old": product.standard_price,
                                                                "wal_new": sheet.cell_value(idx,4)
                                    }))
                                    #adapt the price
                                    product.list_price = sheet.cell_value(idx,6)
                                    product.standard_price = sheet.cell_value(idx,4)
                    idx += 1 
        ## ? Same question than before : is it better to user vals[''] or res ? 
        # vals["product_modif_ids"] = product_array
        res.wal_product_modif_ids = product_array


        return res

    



class ProductModif(models.Model):
    _name = "adaptor.product"
    _description = "Product modifications"
    wal_product_id = fields.Many2one("product.template", string="product")
    wal_field_type = fields.Char("field modified")
    wal_old = fields.Float("Old value")
    wal_new = fields.Float("New value")
    wal_adaptor_resume_id = fields.Many2one("adaptor.resume", string= "Adaptment" , required=True, readonly=True, auto_join=True)
    wal_date_modif_resume = fields.Date(related='wal_adaptor_resume_id.wal_date_modif')

class ImportProperty(models.Model):
    _name = "adaptor.import.property"
    _description = "Properties for the import"
    wal_adaptor_resume_id = fields.Many2one("adaptor.resume", string= "Adaptment" , required=True, readonly=True, auto_join=True)
    ## ?same field present in model adaptor resume, maybe another way to not copy past ? 
    wal_col_excel_import = fields.Integer("column number to import : a =1, b=2, etc...")
    wal_field_related_to_col = fields.Selection(selection=lambda self: self.dynamic_selection_fields())

    ## ?same field present in model adaptor resume, maybe another way to not copy past ? 
    #check and return all the available fields for product.template
    def dynamic_selection_fields(self):
        select_dict = self.env['product.template']._fields
        select_list = []
        for key, val in select_dict.items():
            select_list.append((key, key))

        return select_list