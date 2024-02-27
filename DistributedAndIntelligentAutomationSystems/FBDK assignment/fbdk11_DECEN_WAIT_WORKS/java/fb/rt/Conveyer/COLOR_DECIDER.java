/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.Conveyer;
import fb.datatype.*;
import fb.rt.*;
import fb.rt.mva.VSTYLE;
/** FUNCTION_BLOCK COLOR_DECIDER (* Basic Function Block Type *)
  * @author JHC
  * @version 20230329/JHC - Generated.
  */
public class COLOR_DECIDER extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state RED. */
public static final int INDEX_RED = 1;
/** The index (2) of state BLUE. */
public static final int INDEX_BLUE = 2;
/** The index (3) of state YELLOW. */
public static final int INDEX_YELLOW = 3;
/** Execution Confirmation */
public final EventOutput CNF = new EventOutput();
/** EVENT RED */
public final EventServer RED = (e) -> service_RED();
/** EVENT BLUE */
public final EventServer BLUE = (e) -> service_BLUE();
/** EVENT YELLOW */
public final EventServer YELLOW = (e) -> service_YELLOW();
/** VAR STYLE_IN:VSTYLE */
  public VSTYLE STYLE_IN = new VSTYLE();
/** VAR RED_IN:COLOR */
  public COLOR RED_IN = new COLOR();
/** VAR YELLOW_IN:COLOR */
  public COLOR YELLOW_IN = new COLOR();
/** VAR BLUE_IN:COLOR */
  public COLOR BLUE_IN = new COLOR();
/** VAR POS:UINT */
  public final UINT POS = new UINT("0");
/** VAR STYLE:VSTYLE */
  public final VSTYLE STYLE = new VSTYLE("PALLET");
/** VAR WKPC:COLOR */
  public final COLOR WKPC = new COLOR();
/** The default constructor. */
public COLOR_DECIDER(){
    super();
  }
protected synchronized void service_RED(){
  if(eccState == INDEX_START){
    state_RED();
  }
}
protected synchronized void service_BLUE(){
  if(eccState == INDEX_START){
    state_BLUE();
  }
}
protected synchronized void service_YELLOW(){
  if(eccState == INDEX_START){
    state_YELLOW();
  }
}
/** The actions to take upon entering state START. */
void state_START(){
   eccState = INDEX_START;
}
/** The actions to take upon entering state RED. */
void state_RED(){
   eccState = INDEX_RED;
   alg_RED_ALG();
   CNF.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state BLUE. */
void state_BLUE(){
   eccState = INDEX_BLUE;
   alg_BLUE_ALG();
   CNF.serviceEvent(this);
   state_START();
}
/** The actions to take upon entering state YELLOW. */
void state_YELLOW(){
   eccState = INDEX_YELLOW;
   alg_YELLOW_ALG();
   CNF.serviceEvent(this);
   state_START();
}
  /** ALGORITHM RED_ALG IN ST */
public void alg_RED_ALG(){
POS.value = 0;
STYLE.value = STYLE_IN.value;
WKPC.value = RED_IN.value;
}
  /** ALGORITHM YELLOW_ALG IN ST */
public void alg_YELLOW_ALG(){
POS.value = 0;
STYLE.value = STYLE_IN.value;
WKPC.value = YELLOW_IN.value;
}
  /** ALGORITHM BLUE_ALG IN ST */
public void alg_BLUE_ALG(){
POS.value = 0;
STYLE.value = STYLE_IN.value;
WKPC.value = BLUE_IN.value;
}
}
