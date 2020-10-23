package org.uab.solid;

import java.util.List;

public class LibraryManager {
    private RepositoryBook repositoryBook;
    public LibraryManager(RepositoryBook repositoryBook){
        this.repositoryBook = repositoryBook;
    }
    public Shelf buildHistoryShelf(){
        List<Book> listBook = repositoryBook.viewListBooks();
        Shelf shelf = new Shelf("History Shelf");
        for (Book book :listBook) {
            shelf.addProduct(book);
        }//end for
        return shelf;
    }//end function
}//end class
