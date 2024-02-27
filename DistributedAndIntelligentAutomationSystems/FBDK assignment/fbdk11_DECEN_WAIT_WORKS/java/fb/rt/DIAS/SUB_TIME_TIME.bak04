/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.DIAS;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK SUB_TIME_TIME (* a simple FB Function Block Type *)
  * @author JHC
  * @version 20230327/JHC - Generated.
  */
public class SUB_TIME_TIME extends fb.rt.FBInstance {
/** Confirmation of Requested Service */
public final EventOutput CNF = new EventOutput();
/** Service Request */
public final EventServer REQ = (e) -> {
  alg_REQ();
  CNF.serviceEvent(this);
  }
;
/** EVENT RESET */
public final EventServer RESET = (e) -> {
  alg_RESET_ALG();
  }
;
/** Input Variable */
  public TIME IN_1 = new TIME();
/** VAR IN_2:TIME */
  public TIME IN_2 = new TIME("t#1s");
/** Output variable */
  public final TIME OUT = new TIME();
/** VAR MULT:INT */
  public INT MULT = new INT("0");
/** The default constructor. */
public SUB_TIME_TIME(){
    super();
  }
  /** ALGORITHM REQ IN ST
 * Normally Executed Algorithm
 */
public void alg_REQ(){
OUT.value = IN_1.value - MULT.value*IN_2.value;
MULT.value =(short)( MULT.value + 1);
}
  /** ALGORITHM RESET_ALG IN ST */
public void alg_RESET_ALG(){
MULT.value =(short)( 0);
}
}
