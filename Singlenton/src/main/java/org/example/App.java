package org.example;

import java.sql.SQLException;

public class App
{
    public static void main( String[] args ) throws SQLException, ClassNotFoundException {
        RepositoryBook repositoryBook = new RepositoryBook();
        for (Book book: repositoryBook.viewListBooks()) {
            System.out.println(book.getTitle());
        }
    }//end main
}//end class
