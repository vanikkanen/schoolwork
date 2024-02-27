/* Copyright (c)2023 Rockwell Automation. All rights reserved. */
package fb.rt.Conveyer;
import fb.datatype.*;
import fb.rt.*;
import fb.rt.events.E_PERMIT;
import fb.rt.math.FB_AND;
/** FUNCTION_BLOCK CNV_MERGE_MDL (* Composite Function Block Type *)
  * @author JHC
  * @version 20230329/JHC - Generated.
  */
public class CNV_MERGE_MDL extends fb.rt.FBInstance {
/** EVENT CNF */
public final EventOutput CNF = new EventOutput();
/** EVENT REQ */
public final EventServer REQ = (e) -> service_REQ();
/** FB and1:FB_AND */
  protected FB_AND and1 = new FB_AND() ;
/** FB and2:FB_AND */
  protected FB_AND and2 = new FB_AND() ;
/** FB permit:E_PERMIT */
  protected E_PERMIT permit = new E_PERMIT() ;
/** VAR IN_CNV_M:BOOL */
  public BOOL IN_CNV_M = new BOOL();
/** VAR IN_CNV_OUT:BOOL */
  public BOOL IN_CNV_OUT = new BOOL();
/** VAR IN_CNV_END:BOOL */
  public BOOL IN_CNV_END = new BOOL();
/** The default constructor. */
public CNV_MERGE_MDL(){
    super();
    and1.CNF.connectTo(and2.REQ);
    and2.CNF.connectTo(permit.EI);
    permit.EO.connectTo(CNF);
    and2.connectIVNoException("IN1",and1.ovNamedNoException("OUT"));
    and1.connectIVNoException("IN1",IN_CNV_M);
    and1.connectIVNoException("IN2",IN_CNV_OUT);
    and2.connectIVNoException("IN2",IN_CNV_END);
    permit.connectIVNoException("PERMIT",and2.ovNamedNoException("OUT"));
  }
	/**
 * {@inheritDoc}
 * @param newVar {@inheritDoc}
 */
@Override
protected void connectInternal(ANY newVar) {
  if(newVar == IN_CNV_M)
    and1.connectIVNoException("IN1",IN_CNV_M);
  if(newVar == IN_CNV_OUT)
    and1.connectIVNoException("IN2",IN_CNV_OUT);
  if(newVar == IN_CNV_END)
    and2.connectIVNoException("IN2",IN_CNV_END);
}
/** start the FB instances. */
public void start( ){
    super.start();
  and1.start();
  and2.start();
  permit.start();
}
/** stop the FB instances. */
public void stop( ){
    super.stop();
  and1.stop();
  and2.stop();
  permit.stop();
}
/** kill the FB instances. */
public void kill( ){
    super.kill();
  and1.kill();
  and2.kill();
  permit.kill();
}
/** reset the FB instances. */
public void reset( ){
    super.reset();
  and1.reset();
  and2.reset();
  permit.reset();
}
protected synchronized void service_REQ(){
   and1.REQ.serviceEvent(this);
}
/** {@inheritDoc}
 * @param fbName {@inheritDoc}
 * @param r {@inheritDoc}
 * @throws FBRManagementException {@inheritDoc} */
  public void initialize(String fbName, Resource r)
  throws FBRManagementException{
    super.initialize(fbName,r);
    and1.initialize("and1",r);
    and2.initialize("and2",r);
    permit.initialize("permit",r);
}
}
