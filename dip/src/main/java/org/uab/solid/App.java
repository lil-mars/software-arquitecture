package org.uab.solid;

import java.io.IOException;
import java.sql.SQLException;

public class App
{
    public static void main( String[] args ) throws IOException, SQLException, ClassNotFoundException {
        System.out.println("SHOW  Products: ");
        LibraryManager libraryManager = new LibraryManager(new RepositoryBook());
        Controller controller = new Controller(libraryManager, new ConsoleUI());
        controller.showLibrary();
     }
}
