package org.example;
// clase Pizza es el Producto
public class Pizza {
    private String masa;
    private String salsa;
    private String cobertura;

    public void setMasa(String masa) {
        this.masa = masa;
    }

    public void setCobertura(String cobertura) {
        this.cobertura = cobertura;
    }

    public void setSalsa(String salsa) {
        this.salsa = salsa;
    }

    @Override
    public String toString() {
        return "Pizza{" +
                "masa='" + masa + '\'' +
                ", salsa='" + salsa + '\'' +
                ", cobertura='" + cobertura + '\'' +
                '}';
    }
}//end class
