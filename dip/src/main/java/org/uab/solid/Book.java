package org.uab.solid;

public class Book implements IProduct{
    private int idBook;
    private String title;
    private String sample;

    public int getIdBook() {
        return idBook;
    }
    public String getTitle() {
        return title;
    }
    public String getSample(){
        return sample;
    }
    public void setIdBook(int idBook) {
        this.idBook = idBook;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    public void setSample(String sample) {
        this.sample = sample;
    }
}
