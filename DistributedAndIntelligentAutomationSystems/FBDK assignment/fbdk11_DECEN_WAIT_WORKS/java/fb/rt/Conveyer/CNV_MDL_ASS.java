/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.Conveyer;
import fb.datatype.*;
import fb.rt.*;
import fb.rt.mva.VSTYLE;
/** FUNCTION_BLOCK CNV_MDL_ASS (* Simple Conveyor Model for 1 Workpiece *)
  * @author JHC
  * @version 20230329/JHC - Generated.
  */
public class CNV_MDL_ASS extends fb.rt.FBInstance {
/** The index (0) of state START. */
public static final int INDEX_START = 0;
/** The index (1) of state LOAD. */
public static final int INDEX_LOAD = 1;
/** The index (2) of state UNLD. */
public static final int INDEX_UNLD = 2;
/** The index (3) of state CLK. */
public static final int INDEX_CLK = 3;
/** The index (4) of state INDS. */
public static final int INDEX_INDS = 4;
/** Change in Rendering Data */
public final EventOutput INDR = new EventOutput();
/** Change in Sensor Data */
public final EventOutput INDS = new EventOutput();
/** EVENT UNLD_DATA */
public final EventOutput UNLD_DATA = new EventOutput();
/** Simulation Clock Event */
public final EventServer CLK = (e) -> service_CLK();
/** Load Workpiece if at HOME position */
public final EventServer LOAD = (e) -> service_LOAD();
/** Unload Workpiece if at END position */
public final EventServer UNLD = (e) -> service_UNLD();
/** Motor ON command */
  public BOOL MTR_ON = new BOOL();
/** Fault Condition */
  public BOOL FAULT = new BOOL();
/** Conveyor Speed in % per CLK event */
  public UINT VF = new UINT();
/** Load Position in % of Conveyor Length */
  public UINT LPOS = new UINT();
/** Input Workpiece style */
  public VSTYLE STYLE = new VSTYLE("NONE");
/** Input Workpiece Color */
  public COLOR WKPC = new COLOR("yellow");
/** Workpiece at End Position */
  public final BOOL END = new BOOL();
/** Workpiece Position in % of Conveyor Length */
  public final UINT POS = new UINT();
/** Currently loaded workpiece style */
  public final VSTYLE STYLO = new VSTYLE("NONE");
/** Currently loaded workpiece color */
  public final COLOR WKPO = new COLOR("blue");
/** STYLO = VSTYLE#NONE */
  public BOOL EMPTY = new BOOL("TRUE");
/** The default constructor. */
public CNV_MDL_ASS(){
    super();
  }
protected synchronized void service_CLK(){
  if((eccState == INDEX_START) && (MTR_ON.value && ! FAULT.value && ! EMPTY.value && ! END.value)){
    state_CLK();
  }
}
protected synchronized void service_LOAD(){
  if((eccState == INDEX_START) && (EMPTY.value)){
    state_LOAD();
  }
}
protected synchronized void service_UNLD(){
  if((eccState == INDEX_START) && (! EMPTY.value)){
    state_UNLD();
  }
}
/** The actions to take upon entering state START. */
void state_START(){
   eccState = INDEX_START;
}
/** The actions to take upon entering state LOAD. */
void state_LOAD(){
   eccState = INDEX_LOAD;
   alg_LOAD();
   INDR.serviceEvent(this);
   state_INDS();
}
/** The actions to take upon entering state UNLD. */
void state_UNLD(){
   eccState = INDEX_UNLD;
   alg_UNLD();
   INDR.serviceEvent(this);
   UNLD_DATA.serviceEvent(this);
   state_INDS();
}
/** The actions to take upon entering state CLK. */
void state_CLK(){
   eccState = INDEX_CLK;
   alg_CLK();
   INDR.serviceEvent(this);
   if(END.value)
     state_INDS();
   if(! END.value)
     state_START();
}
/** The actions to take upon entering state INDS. */
void state_INDS(){
   eccState = INDEX_INDS;
   INDS.serviceEvent(this);
   state_START();
}
  /** ALGORITHM LOAD IN Java */
public void alg_LOAD(){
POS.value = Math.min(100,LPOS.value);
END.value = (POS.value==100)&&(STYLE.value != VSTYLE.NONE);
STYLO.value = STYLE.value;
WKPO.value = WKPC.value;
EMPTY.value = (STYLE.value == VSTYLE.NONE);
}
  /** ALGORITHM UNLD IN Java */
public void alg_UNLD(){
STYLO.value=VSTYLE.NONE;
END.value = false;
EMPTY.value = true;
}
  /** ALGORITHM CLK IN Java */
public void alg_CLK(){
POS.value += VF.value;
if(POS.value>=100){
POS.value=100;
END.value=true;}
}
}
