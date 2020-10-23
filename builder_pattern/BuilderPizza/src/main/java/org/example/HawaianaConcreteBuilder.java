package org.example;

public class HawaianaConcreteBuilder extends PizzaBuilder{
    @Override
    public void buildMasa() {
        pizza.setMasa("Suave");
    }

    @Override
    public void buildSalsa() {
        pizza.setSalsa("dulce");
    }


    @Override
    public void buildCobertura() {
        pizza.setCobertura("pina + durazno");
    }

}
