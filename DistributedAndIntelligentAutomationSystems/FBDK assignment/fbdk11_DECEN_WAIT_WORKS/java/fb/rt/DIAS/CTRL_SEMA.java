/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.DIAS;
import fb.datatype.*;
import fb.rt.*;
/** FUNCTION_BLOCK CTRL_SEMA (* Basic Function Block Type *)
  * @author JHC
  * @version 20230327/JHC - Generated.
  */
public class CTRL_SEMA extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state INIT. */
public static final int INDEX_INIT = 1;
/** The index (2) of state GREEN_I. */
public static final int INDEX_GREEN_I = 2;
/** The index (3) of state YELLOW_I. */
public static final int INDEX_YELLOW_I = 3;
/** The index (4) of state PREV_CTRL. */
public static final int INDEX_PREV_CTRL = 4;
/** The index (5) of state UPDATE_TIME. */
public static final int INDEX_UPDATE_TIME = 5;
/** Initialization Confirm */
public final EventOutput INITO = new EventOutput();
/** EVENT GREEN_O */
public final EventOutput GREEN_O = new EventOutput();
/** EVENT YELLOW_O */
public final EventOutput YELLOW_O = new EventOutput();
/** EVENT NEXT_CTRL */
public final EventOutput NEXT_CTRL = new EventOutput();
/** Initialization Request */
public final EventServer INIT = (e) -> service_INIT();
/** EVENT GREEN_I */
public final EventServer GREEN_I = (e) -> service_GREEN_I();
/** EVENT YELLOW_I */
public final EventServer YELLOW_I = (e) -> service_YELLOW_I();
/** EVENT PREV_CTRL */
public final EventServer PREV_CTRL = (e) -> service_PREV_CTRL();
/** EVENT UPDATE_TIME */
public final EventServer UPDATE_TIME = (e) -> service_UPDATE_TIME();
/** VAR GREEN_TIME:TIME */
  public TIME GREEN_TIME = new TIME();
/** VAR YELLOW_TIME:TIME */
  public TIME YELLOW_TIME = new TIME();
/** VAR MODE:INT */
  public final INT MODE = new INT();
/** VAR TIME_OUT:TIME */
  public final TIME TIME_OUT = new TIME();
/** The default constructor. */
public CTRL_SEMA(){
    super();
  }
protected synchronized void service_INIT(){
  if(eccState == INDEX_START){
    state_INIT();
  }
}
protected synchronized void service_GREEN_I(){
  if(eccState == INDEX_START){
    state_GREEN_I();
  }
}
protected synchronized void service_YELLOW_I(){
  if(eccState == INDEX_START){
    state_YELLOW_I();
  }
}
protected synchronized void service_PREV_CTRL(){
  if(eccState == INDEX_START){
    state_PREV_CTRL();
  }
}
protected synchronized void service_UPDATE_TIME(){
  if(eccState == INDEX_START){
    state_UPDATE_TIME();
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
/** The actions to take upon entering state GREEN_I. */
void state_GREEN_I(){
   eccState = INDEX_GREEN_I;
   alg_YELLOW_LIGHT_ALG();
   YELLOW_O.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state YELLOW_I. */
void state_YELLOW_I(){
   eccState = INDEX_YELLOW_I;
   alg_RED_LIGHT_ALG();
   NEXT_CTRL.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state PREV_CTRL. */
void state_PREV_CTRL(){
   eccState = INDEX_PREV_CTRL;
   alg_GREEN_LIGHT_ALG();
   GREEN_O.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state UPDATE_TIME. */
void state_UPDATE_TIME(){
   eccState = INDEX_UPDATE_TIME;
   state_START();
}
  /** ALGORITHM INIT IN ST
 * Initialization algorithm
 */
public void alg_INIT(){
MODE.value =(short)( 0);
}
  /** ALGORITHM GREEN_LIGHT_ALG IN ST */
public void alg_GREEN_LIGHT_ALG(){
MODE.value =(short)( 2);
TIME_OUT.value = GREEN_TIME.value;
}
  /** ALGORITHM YELLOW_LIGHT_ALG IN ST */
public void alg_YELLOW_LIGHT_ALG(){
MODE.value =(short)( 1);
TIME_OUT.value = YELLOW_TIME.value;
}
  /** ALGORITHM RED_LIGHT_ALG IN ST */
public void alg_RED_LIGHT_ALG(){
MODE.value =(short)( 0);
}
}
