package org.example;

public class ExpresionCientos extends Expression {
    @Override
    public String Unidad() { return "C"; }

    @Override
    public String Cuatro() { return "CD"; }

    @Override
    public String Cinco() { return "D"; }

    @Override
    public String Nueve() { return "CM"; }

    @Override
    public int Factor() { return 100; }
}
