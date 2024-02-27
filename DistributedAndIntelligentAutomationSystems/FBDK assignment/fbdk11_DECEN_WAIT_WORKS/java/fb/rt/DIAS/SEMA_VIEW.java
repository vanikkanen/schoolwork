/* Copyright (c)2023 Holobloc Inc. All rights reserved. */
package fb.rt.DIAS;
import fb.datatype.*;
import fb.rt.*;
import fb.rt.hmi.*;
/** FUNCTION_BLOCK SEMA_VIEW
  * @author JHC
  * @version 20230327/JHC - Generated.
  */
public class SEMA_VIEW extends fb.rt.FBInstance {
/** INIT Confirm */
public final EventOutput INITO = new EventOutput();
/** REQ Confirmation */
public final EventOutput CNF = new EventOutput();
/** Initialize */
public final EventServer INIT = (e) -> service_INIT();
/** LED State/Color Update */
public final EventServer REQ = (e) -> service_REQ();
/** FB OUT2:OUT_BOOL */
  protected OUT_BOOL OUT2 = new OUT_BOOL() ;
/** FB OUT1:OUT_BOOL */
  protected OUT_BOOL OUT1 = new OUT_BOOL() ;
/** FB OUT0:OUT_BOOL */
  protected OUT_BOOL OUT0 = new OUT_BOOL() ;
/** Synchronize frame buffer */
  protected PANEL_SYNC SYNC = new PANEL_SYNC() ;
/** VAR LED2:BOOL */
  public BOOL LED2 = new BOOL();
/** VAR LED1:BOOL */
  public BOOL LED1 = new BOOL();
/** LSB - Least Significant Bit */
  public BOOL LED0 = new BOOL();
/** OFF color */
  public COLOR C0 = new COLOR("COLOR#white");
/** ON color */
  public COLOR C1 = new COLOR("COLOR#orange");
/** The default constructor. */
public SEMA_VIEW(){
    super();
    OUT2.INITO.connectTo(OUT1.INIT);
    OUT1.INITO.connectTo(OUT0.INIT);
    OUT0.INITO.connectTo(INITO);
    OUT2.CNF.connectTo(OUT1.REQ);
    OUT1.CNF.connectTo(OUT0.REQ);
    OUT0.CNF.connectTo(SYNC.REQ);
    SYNC.CNF.connectTo(CNF);
    OUT2.connectIVNoException("IN",LED2);
    OUT1.connectIVNoException("IN",LED1);
    OUT0.connectIVNoException("IN",LED0);
    OUT2.connectIVNoException("C0",C0);
    OUT1.connectIVNoException("C0",C0);
    OUT0.connectIVNoException("C0",C0);
    OUT2.connectIVNoException("C1",C1);
    OUT1.connectIVNoException("C1",C1);
    OUT0.connectIVNoException("C1",C1);
    OUT2.QI.initializeNoException("1");
    OUT2.LABEL.initializeNoException("GREEN");
    OUT1.QI.initializeNoException("1");
    OUT1.LABEL.initializeNoException("YELLOW");
    OUT0.QI.initializeNoException("1");
    OUT0.LABEL.initializeNoException("RED");
    SYNC.QI.initializeNoException("1");
  }
	/**
 * {@inheritDoc}
 * @param newVar {@inheritDoc}
 */
@Override
protected void connectInternal(ANY newVar) {
  if(newVar == LED2)
    OUT2.connectIVNoException("IN",LED2);
  if(newVar == LED1)
    OUT1.connectIVNoException("IN",LED1);
  if(newVar == LED0)
    OUT0.connectIVNoException("IN",LED0);
  if(newVar == C0)
    OUT2.connectIVNoException("C0",C0);
  if(newVar == C0)
    OUT1.connectIVNoException("C0",C0);
  if(newVar == C0)
    OUT0.connectIVNoException("C0",C0);
  if(newVar == C1)
    OUT2.connectIVNoException("C1",C1);
  if(newVar == C1)
    OUT1.connectIVNoException("C1",C1);
  if(newVar == C1)
    OUT0.connectIVNoException("C1",C1);
}
/** start the FB instances. */
public void start( ){
    super.start();
  OUT2.start();
  OUT1.start();
  OUT0.start();
  SYNC.start();
}
/** stop the FB instances. */
public void stop( ){
    super.stop();
  OUT2.stop();
  OUT1.stop();
  OUT0.stop();
  SYNC.stop();
}
/** kill the FB instances. */
public void kill( ){
    super.kill();
  OUT2.kill();
  OUT1.kill();
  OUT0.kill();
  SYNC.kill();
}
/** reset the FB instances. */
public void reset( ){
    super.reset();
  OUT2.reset();
  OUT1.reset();
  OUT0.reset();
  SYNC.reset();
}
protected synchronized void service_INIT(){
   OUT2.INIT.serviceEvent(this);
}
protected synchronized void service_REQ(){
   OUT2.REQ.serviceEvent(this);
}
/** {@inheritDoc}
 * @param fbName {@inheritDoc}
 * @param r {@inheritDoc}
 * @throws FBRManagementException {@inheritDoc} */
  public void initialize(String fbName, Resource r)
  throws FBRManagementException{
    super.initialize(fbName,r);
    OUT2.initialize("OUT2",r);
    OUT1.initialize("OUT1",r);
    OUT0.initialize("OUT0",r);
    SYNC.initialize("SYNC",r);
}
}
