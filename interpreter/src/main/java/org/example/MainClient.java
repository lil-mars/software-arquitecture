package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MainClient
{
    public static void main( String[] args )
    {
        String exprexionAEvaluar = "MMMCMXIX";

        //String exprexionAEvaluar = "CD";
        Context context = new Context(exprexionAEvaluar);
        List<Expression> arbol = new ArrayList<>();
        arbol.add(new ExpresionMiles());
        arbol.add(new ExpresionCientos());
        arbol.add(new ExpresionDecenas());
        arbol.add(new ExpresionUnidad());
        for (Expression expression : arbol) {
            expression.interpretar(context);
        }
        System.out.println("El numero romano " + exprexionAEvaluar + " es " + context.getValor() + " en decimal" );
    }//end main
}//end class
