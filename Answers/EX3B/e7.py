class Product:
    tax_rate = 0.1
    
    def apply_discount(self, new_rate):
        Product.tax_rate = new_rate
    