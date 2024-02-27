/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.Conveyer;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK SENSOR_MODEL (* Basic Function Block Type *)
  * @author JHC
  * @version 20230329/JHC - Generated.
  */
public class SENSOR_MODEL extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state INIT. */
public static final int INDEX_INIT = 1;
/** The index (2) of state REQ. */
public static final int INDEX_REQ = 2;
/** Initialization Confirm */
public final EventOutput INITO = new EventOutput();
/** Execution Confirmation */
public final EventOutput CNF = new EventOutput();
/** Initialization Request */
public final EventServer INIT = (e) -> service_INIT();
/** Normal Execution Request */
public final EventServer REQ = (e) -> service_REQ();
/** VAR STATUS_IN:BOOL */
  public BOOL STATUS_IN = new BOOL();
/** VAR STATUS:BOOL */
  public final BOOL STATUS = new BOOL();
/** The default constructor. */
public SENSOR_MODEL(){
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
/** The actions to take upon entering state REQ. */
void state_REQ(){
   eccState = INDEX_REQ;
   alg_REQ();
   CNF.serviceEvent(this);
   state_START();
}
  /** ALGORITHM INIT IN ST
 * Initialization algorithm
 */
public void alg_INIT(){
STATUS.value = false;
}
  /** ALGORITHM REQ IN ST
 * Normally executed algorithm
 */
public void alg_REQ(){
STATUS.value = STATUS_IN.value;
}
}
