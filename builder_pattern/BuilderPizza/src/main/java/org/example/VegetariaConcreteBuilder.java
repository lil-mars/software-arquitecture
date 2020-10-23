package org.example;

public class VegetariaConcreteBuilder extends PizzaBuilder {
    @Override
    public void buildMasa() {
        pizza.setMasa("Suave");
    }

    @Override
    public void buildSalsa() {
        pizza.setSalsa("criolla");
    }

    @Override
    public void buildCobertura() {
        pizza.setCobertura("verduras de la temporada + gluten");
    }

}//end class
