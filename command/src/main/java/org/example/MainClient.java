package org.example;
import java.util.Scanner;

public class MainClient
{
    public static void main( String[] args )
    {   Scanner scanner = new Scanner(System.in);
        int opcion;
        Automovil auto = new Automovil();
        ControlRemoto controlRemoto = new ControlRemoto(auto);

        do{
            System.out.println("==== Comandos que desea realizar en el auto ====");
            System.out.println("1. Encender Auto; 2. Apagar Auto; 3. Encender Alarma; 4. Apagar Alarma; 5. Salir ");
            opcion = scanner.nextInt();
            if(opcion == 1){
                //EncenderAuto
                controlRemoto.presionarBoton(0);
            }
            if(opcion == 2){
                //ApagarAuto
                controlRemoto.presionarBoton(1);
            }
            if(opcion == 3){
                //EncenderAlarma
                controlRemoto.presionarBoton(2);
            }
            if(opcion == 4){
                //ApagarAlarma
                controlRemoto.presionarBoton(3);
            }
        }
        while(opcion != 5);
    }//end manin
}//end class main
