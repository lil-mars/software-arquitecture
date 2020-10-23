package org.example;

public abstract class PizzaBuilder {
    protected Pizza pizza;

    public Pizza getPizza() {
        return pizza;
    }
    public void createNuevaPizza(){
        pizza = new Pizza();
    }
    protected abstract void buildMasa();
    protected abstract void buildSalsa();
    protected abstract void buildCobertura();
}
