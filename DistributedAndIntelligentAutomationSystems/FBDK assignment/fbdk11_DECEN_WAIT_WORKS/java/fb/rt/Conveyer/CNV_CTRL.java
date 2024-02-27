/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.Conveyer;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK CNV_CTRL (* Basic Function Block Type *)
  * @author JHC
  * @version 20230329/JHC - Generated.
  */
public class CNV_CTRL extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state INIT. */
public static final int INDEX_INIT = 1;
/** The index (2) of state REQ. */
public static final int INDEX_REQ = 2;
/** The index (3) of state UNLOAD. */
public static final int INDEX_UNLOAD = 3;
/** The index (4) of state LOAD. */
public static final int INDEX_LOAD = 4;
/** The index (5) of state START_MOTOR. */
public static final int INDEX_START_MOTOR = 5;
/** The index (6) of state TURN_OFF_MOTOR. */
public static final int INDEX_TURN_OFF_MOTOR = 6;
/** Initialization Confirm */
public final EventOutput INITO = new EventOutput();
/** Execution Confirmation */
public final EventOutput CNF = new EventOutput();
/** EVENT UNLOAD_OUT */
public final EventOutput UNLOAD_OUT = new EventOutput();
/** EVENT LOAD_OUT */
public final EventOutput LOAD_OUT = new EventOutput();
/** Initialization Request */
public final EventServer INIT = (e) -> service_INIT();
/** Normal Execution Request */
public final EventServer REQ = (e) -> service_REQ();
/** EVENT LOAD */
public final EventServer LOAD = (e) -> service_LOAD();
/** EVENT UNLOAD */
public final EventServer UNLOAD = (e) -> service_UNLOAD();
/** EVENT START_MOTOR */
public final EventServer START_MOTOR = (e) -> service_START_MOTOR();
/** EVENT TURN_OFF_MOTOR */
public final EventServer TURN_OFF_MOTOR = (e) -> service_TURN_OFF_MOTOR();
/** VAR MOTOR_OUT:BOOL */
  public final BOOL MOTOR_OUT = new BOOL();
/** The default constructor. */
public CNV_CTRL(){
    super();
  }
protected synchronized void service_INIT(){
  if(eccState == INDEX_START){
    state_INIT();
  }
}
protected synchronized void service_REQ(){
  if(eccState == INDEX_START){
    state_REQ();
  }
}
protected synchronized void service_LOAD(){
  if(eccState == INDEX_START){
    state_LOAD();
  }
}
protected synchronized void service_UNLOAD(){
  if(eccState == INDEX_START){
    state_UNLOAD();
  }
}
protected synchronized void service_START_MOTOR(){
  if(eccState == INDEX_START){
    state_START_MOTOR();
  }
}
protected synchronized void service_TURN_OFF_MOTOR(){
  if(eccState == INDEX_START){
    state_TURN_OFF_MOTOR();
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
   state_START_MOTOR();
}
/** The actions to take upon entering state REQ. */
void state_REQ(){
   eccState = INDEX_REQ;
   alg_REQ();
   CNF.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state UNLOAD. */
void state_UNLOAD(){
   eccState = INDEX_UNLOAD;
   UNLOAD_OUT.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state LOAD. */
void state_LOAD(){
   eccState = INDEX_LOAD;
   LOAD_OUT.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state START_MOTOR. */
void state_START_MOTOR(){
   eccState = INDEX_START_MOTOR;
   alg_START_MOTOR_ALG();
   CNF.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state TURN_OFF_MOTOR. */
void state_TURN_OFF_MOTOR(){
   eccState = INDEX_TURN_OFF_MOTOR;
   alg_TURN_OFF_MOTOR();
   CNF.serviceEvent(this);
   state_START();
}
  /** ALGORITHM INIT IN ST
 * Initialization algorithm
 */
public void alg_INIT(){
MOTOR_OUT.value = true;
}
  /** ALGORITHM REQ IN ST
 * Normally executed algorithm
 */
public void alg_REQ(){
}
  /** ALGORITHM START_MOTOR_ALG IN ST */
public void alg_START_MOTOR_ALG(){
MOTOR_OUT.value = true;
}
  /** ALGORITHM TURN_OFF_MOTOR IN ST */
public void alg_TURN_OFF_MOTOR(){
MOTOR_OUT.value = false;
}
}
