/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.Conveyer;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK MOTOR_TO_EVENTS (* Basic Function Block Type *)
  * @author JHC
  * @version 20230329/JHC - Generated.
  */
public class MOTOR_TO_EVENTS extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state INIT. */
public static final int INDEX_INIT = 1;
/** The index (2) of state M_ON. */
public static final int INDEX_M_ON = 2;
/** The index (3) of state M_OFF. */
public static final int INDEX_M_OFF = 3;
/** Initialization Confirm */
public final EventOutput INITO = new EventOutput();
/** EVENT START_MOTOR */
public final EventOutput START_MOTOR = new EventOutput();
/** EVENT STOP_MOTOR */
public final EventOutput STOP_MOTOR = new EventOutput();
/** Initialization Request */
public final EventServer INIT = (e) -> service_INIT();
/** Normal Execution Request */
public final EventServer REQ = (e) -> service_REQ();
/** EVENT M_ON */
public final EventServer M_ON = (e) -> service_M_ON();
/** EVENT M_OFF */
public final EventServer M_OFF = (e) -> service_M_OFF();
/** VAR MOTOR_IN:BOOL */
  public BOOL MOTOR_IN = new BOOL();
/** The default constructor. */
public MOTOR_TO_EVENTS(){
    super();
  }
protected synchronized void service_INIT(){
  if(eccState == INDEX_START){
    state_INIT();
  }
}
protected synchronized void service_REQ(){
  if((eccState == INDEX_START) && (MOTOR_IN.value)){
    state_M_ON();
  }
  else if((eccState == INDEX_START) && (! MOTOR_IN.value)){
    state_M_OFF();
  }
}
protected synchronized void service_M_ON(){
  if((eccState == INDEX_START) && (MOTOR_IN.value)){
    state_M_ON();
  }
}
protected synchronized void service_M_OFF(){
  if((eccState == INDEX_START) && (! MOTOR_IN.value)){
    state_M_OFF();
  }
}
/** The actions to take upon entering state START. */
void state_START(){
   eccState = INDEX_START;
}
/** The actions to take upon entering state INIT. */
void state_INIT(){
   eccState = INDEX_INIT;
   alg_INIT();
   INITO.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state M_ON. */
void state_M_ON(){
   eccState = INDEX_M_ON;
   START_MOTOR.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state M_OFF. */
void state_M_OFF(){
   eccState = INDEX_M_OFF;
   STOP_MOTOR.serviceEvent(this);
   state_START();
}
  /** ALGORITHM INIT IN ST
 * Initialization algorithm
 */
public void alg_INIT(){
}
}
