package org.uab.solid;

public class ConsoleUI extends LibraryUI {
    @Override
    public void  show() {
        for (Shelf shelf : shelfs) {
            System.out.println("[" + shelf.getType() + "]");
            for (IProduct product : shelf.getProducts()) {
                System.out.println(product.getTitle());
            }
        }
    }//end show
}// end class
