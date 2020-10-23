package org.uab.solid;

import java.util.ArrayList;
import java.util.List;

public class Shelf {
    private String type;
    private List<IProduct> products;
    public Shelf(String type) {
        this.type = type;
        products = new ArrayList();
    }
    public void addProduct(IProduct iproduct){
        products.add(iproduct);
    }//endfunction
    public List<IProduct> getProducts() {
        return products;
    }
    public String getType() {
        return type;
    }
}
