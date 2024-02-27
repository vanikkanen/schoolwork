/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.template;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK SUB_TIME_TMIE (* a simple FB Function Block Type *)
  * @author JHC
  * @version 20230327/JHC - Generated.
  */
public class SUB_TIME_TMIE extends fb.rt.FBInstance {
/** Confirmation of Requested Service */
public final EventOutput CNF = new EventOutput();
/** Service Request */
public final EventServer REQ = (e) -> {
  alg_REQ();
  CNF.serviceEvent(this);
  }
;
/** Input Variable */
  public TIME IN_1 = new TIME();
/** VAR IN_2:TIME */
  public TIME IN_2 = new TIME();
/** Output variable */
  public final TIME OUT = new TIME();
/** The default constructor. */
public SUB_TIME_TMIE(){
    super();
  }
  /** ALGORITHM REQ IN ST
 * Normally Executed Algorithm
 */
public void alg_REQ(){
OUT.value = IN_1.value - IN_2.value;
}
}
