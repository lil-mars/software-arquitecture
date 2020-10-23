package org.uab.solid;

public class Controller {
    private final LibraryUI ui;
    private LibraryManager libraryManager;
    public Controller(LibraryManager libraryManager, LibraryUI ui){
        this.libraryManager = libraryManager;
        this.ui = ui;
    }
    public void showLibrary(){
        Shelf shelf = libraryManager.buildHistoryShelf();
        ui.addShelf(shelf);
        ui.show();
    }
}
