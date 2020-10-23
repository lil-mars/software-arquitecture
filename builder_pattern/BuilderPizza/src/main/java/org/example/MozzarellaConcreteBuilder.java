package org.example;

public class MozzarellaConcreteBuilder extends PizzaBuilder{

    @Override
    public void buildMasa() {
        pizza.setMasa("cocida");
    }

    @Override
    public void buildSalsa() {
        pizza.setSalsa("salsa con aji");
    }

    @Override
    public void buildCobertura() {
        pizza.setSalsa("Mozarella+tomates+cebolla");
    }


}//end class
