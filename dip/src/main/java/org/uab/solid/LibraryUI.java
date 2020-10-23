package org.uab.solid;

import java.util.ArrayList;
import java.util.List;

public abstract class LibraryUI {
    protected List<Shelf> shelfs;
    public LibraryUI() {
        shelfs = new ArrayList<>();
    }
    public void addShelf(Shelf shelf) {
        shelfs.add(shelf);
    }
    public abstract void show();
}
