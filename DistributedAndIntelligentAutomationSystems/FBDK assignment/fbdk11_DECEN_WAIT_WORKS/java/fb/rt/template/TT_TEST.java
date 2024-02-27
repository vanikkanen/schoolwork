/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.template;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK TT_TEST (* Basic Function Block Type *)
  * @author JHC
  * @version 20230329/JHC - Generated.
  */
public class TT_TEST extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state INIT. */
public static final int INDEX_INIT = 1;
/** The index (2) of state LOAD. */
public static final int INDEX_LOAD = 2;
/** The index (3) of state TURN_1. */
public static final int INDEX_TURN_1 = 3;
/** The index (4) of state UNLOAD. */
public static final int INDEX_UNLOAD = 4;
/** The index (5) of state TURN_2. */
public static final int INDEX_TURN_2 = 5;
/** Initialization Confirm */
public final EventOutput INITO = new EventOutput();
/** EVENT CNF */
public final EventOutput CNF = new EventOutput();
/** EVENT LOAD */
public final EventOutput LOAD = new EventOutput();
/** EVENT UNLOAD */
public final EventOutput UNLOAD = new EventOutput();
/** EVENT TURN */
public final EventOutput TURN = new EventOutput();
/** Initialization Request */
public final EventServer INIT = (e) -> service_INIT();
/** Normal Execution Request */
public final EventServer REQ = (e) -> service_REQ();
/** VAR CONV_1_STATE:BOOL */
  public BOOL CONV_1_STATE = new BOOL();
/** VAR CONV_2_STATE:BOOL */
  public BOOL CONV_2_STATE = new BOOL();
/** VAR POS_1:BOOL */
  public final BOOL POS_1 = new BOOL();
/** VAR FULL:BOOL */
  public final BOOL FULL = new BOOL();
/** The default constructor. */
public TT_TEST(){
    super();
  }
protected synchronized void service_INIT(){
  if(eccState == INDEX_START){
    state_INIT();
  }
}
protected synchronized void service_REQ(){
  if((eccState == INDEX_START) && (CONV_1_STATE.value)){
    state_LOAD();
  }
  else if((eccState == INDEX_TURN_1) && (CONV_2_STATE.value)){
    state_UNLOAD();
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
/** The actions to take upon entering state LOAD. */
void state_LOAD(){
   eccState = INDEX_LOAD;
   alg_LOAD_ALG();
   CNF.serviceEvent(this);
   LOAD.serviceEvent(this);
   state_TURN_1();
}
/** The actions to take upon entering state TURN_1. */
void state_TURN_1(){
   eccState = INDEX_TURN_1;
   alg_TURN_ALG();
   TURN.serviceEvent(this);
}
/** The actions to take upon entering state UNLOAD. */
void state_UNLOAD(){
   eccState = INDEX_UNLOAD;
   alg_UNLOAD_ALG();
   CNF.serviceEvent(this);
   UNLOAD.serviceEvent(this);
   state_TURN_2();
}
/** The actions to take upon entering state TURN_2. */
void state_TURN_2(){
   eccState = INDEX_TURN_2;
   alg_TURN_ALG();
   TURN.serviceEvent(this);
   state_START();
}
  /** ALGORITHM INIT IN ST
 * Initialization algorithm
 */
public void alg_INIT(){
POS_1.value = true;
FULL.value = false;
}
  /** ALGORITHM LOAD_ALG IN ST */
public void alg_LOAD_ALG(){
FULL.value = true;
}
  /** ALGORITHM TURN_ALG IN ST */
public void alg_TURN_ALG(){
POS_1.value = ! POS_1.value;
}
  /** ALGORITHM UNLOAD_ALG IN ST */
public void alg_UNLOAD_ALG(){
FULL.value = false;
}
}
