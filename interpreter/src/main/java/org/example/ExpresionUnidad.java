package org.example;

public class ExpresionUnidad extends Expression {
    @Override
    public String Unidad(){ return "I"; }
    @Override
    public String Cuatro(){ return "IV"; }
    @Override
    public String Cinco(){ return "V"; }
    @Override
    public String Nueve(){ return "IX"; }
    @Override
    public int Factor(){ return 1; }
}//end class
