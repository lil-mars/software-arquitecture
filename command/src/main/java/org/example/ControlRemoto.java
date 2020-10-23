package org.example;
//Invoker

public class ControlRemoto {
    // Invoker COntrol Remot, puede invokar diferentes comandos
    // entonces se crea una arreglo de comandos
    private ICommando[] iCommandos = new ICommando[4];

    public ControlRemoto(Automovil autoo){
        iCommandos[0] = new ComandoEncenderAuto(autoo);
        iCommandos[1] = new ComandoApagarAuto(autoo);
        iCommandos[2] = new ComandoEncenderAlarma(autoo);
        iCommandos[3] = new ComandoApagarAlarma(autoo);
    }

    public void presionarBoton(int tipoComandoEjecutar){
        iCommandos[tipoComandoEjecutar].ejecutar();
    }
}//end class
