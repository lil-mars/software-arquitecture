package org.example;

public class ExpresionMiles extends Expression {
    @Override
    public String Unidad() {
        return "M";
    }

    @Override
    public String Cuatro() {
        return " ";
    }

    @Override
    public String Cinco() {
        return " ";
    }

    @Override
    public String Nueve() {
        return "    ";
    }

    @Override
    public int Factor() {
        return 1000;
    }
}
