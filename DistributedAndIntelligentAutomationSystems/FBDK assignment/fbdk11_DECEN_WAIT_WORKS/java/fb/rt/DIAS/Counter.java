/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.DIAS;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK Counter (* Basic Function Block Type *)
  * @author JHC
  * @version 20230327/JHC - Generated.
  */
public class Counter extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state REQ. */
public static final int INDEX_REQ = 1;
/** The index (2) of state RESET. */
public static final int INDEX_RESET = 2;
/** The index (3) of state OUTPUT. */
public static final int INDEX_OUTPUT = 3;
/** Execution Confirmation */
public final EventOutput CNF = new EventOutput();
/** Normal Execution Request */
public final EventServer REQ = (e) -> service_REQ();
/** EVENT RESET */
public final EventServer RESET = (e) -> service_RESET();
/** VAR LIMIT:INT */
  public INT LIMIT = new INT();
/** VAR CV:INT */
  public final INT CV = new INT();
/** VAR COUNT:INT */
  public INT COUNT = new INT("1");
/** The default constructor. */
public Counter(){
    super();
  }
protected synchronized void service_REQ(){
  if((eccState == INDEX_START) && (COUNT.value>=LIMIT.value)){
    state_OUTPUT();
  }
  else if(eccState == INDEX_START){
    state_REQ();
  }
}
protected synchronized void service_RESET(){
  if(eccState == INDEX_START){
    state_RESET();
  }
}
/** The actions to take upon entering state START. */
void state_START(){
   eccState = INDEX_START;
}
/** The actions to take upon entering state REQ. */
void state_REQ(){
   eccState = INDEX_REQ;
   alg_REQ();
   state_START();
}
/** The actions to take upon entering state RESET. */
void state_RESET(){
   eccState = INDEX_RESET;
   alg_RESET_ALG();
   state_START();
}
/** The actions to take upon entering state OUTPUT. */
void state_OUTPUT(){
   eccState = INDEX_OUTPUT;
   alg_RESET_ALG();
   CNF.serviceEvent(this);
   state_START();
}
  /** ALGORITHM REQ IN ST */
public void alg_REQ(){
COUNT.value =(short)( COUNT.value+1);
CV.value =(short)( COUNT.value);
}
  /** ALGORITHM RESET_ALG IN ST */
public void alg_RESET_ALG(){
COUNT.value =(short)( 1);
}
}
