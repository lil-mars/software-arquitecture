package org.example;


public class Main
{
    public static void main( String[] args )
    {
        KitchenDirector kitchenDirector = new KitchenDirector();
        PizzaBuilder hawaianaPizzaBuilder = new HawaianaConcreteBuilder();
        //PizzaBuilder mozzarellaPizzaBuilder = new MozzarellaConcreteBuilder();
        kitchenDirector.setPizzaBuilder(hawaianaPizzaBuilder);
        //kitchenDirector.setPizzaBuilder(mozzarellaPizzaBuilder);
        kitchenDirector.construirPizza();
        Pizza pizza = kitchenDirector.getPizza();
        System.out.println(pizza);

    }
}
