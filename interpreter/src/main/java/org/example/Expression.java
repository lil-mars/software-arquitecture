package org.example;

public abstract class Expression {

    public void interpretar(Context context){
        //Verificando si no hay expresion que validar, entonces, salir
        if(context.getExpresion().length() == 0){
            return;
        }
        //Verificando si la expresion comienza con 9
        if(context.getExpresion().startsWith(Nueve())){
            //agregando el nuevo por la posicion donde este: 1, 10, 100
            context.setValor(context.getValor() + (9 * Factor()));
            //eliminando dos caracteres IX, XC, CM
            context.setExpresion(context.getExpresion().substring(2));
        }else if(context.getExpresion().startsWith(Cuatro())){
            //Verificando si la expresion comienza con 4
            context.setValor(context.getValor() + (4 * Factor()));
            //eliminando dos caracteres
            context.setExpresion(context.getExpresion().substring(2));
        }else if(context.getExpresion().startsWith(Cinco())){
            //Verificando si la expresion comienza con 5
            context.setValor(context.getValor() + (5 * Factor()));
            context.setExpresion(context.getExpresion().substring(1));
        }
        //Recorriendo las unidades encontradas: I, X, C
        // II:2, III:3..... XX:20, XXX:30 ...... CC: 200
        while(context.getExpresion().startsWith(Unidad())){
            context.setValor(context.getValor() + (1 * Factor()));
            context.setExpresion(context.getExpresion().substring(1));
        }

    }//end Interpretar
    //Metodos abstractos para encontrar el caracter y factor
    public abstract String Unidad();//I,
    public abstract String Cuatro();
    public abstract String Cinco();
    public abstract String Nueve();
    public abstract int Factor();
}//end class
