package org.example;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class RepositoryBook {
    public RepositoryBook(){ }
    public List<Book> viewListBooks(){
        List<Book> listBook = new ArrayList();
        try{
            Connection connection = JDBCConection.getConnection();
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM book;");
            while(rs.next()) {
                Book book = new Book();
                book.setIdBook(rs.getInt(1));
                book.setTitle(rs.getString(2));
                book.setSample(rs.getString(3));
                listBook.add(book);
            }
        }catch(Exception e){
            System.out.println("Error: "+e);
        }
        return listBook;
    }//end function
}//end class
