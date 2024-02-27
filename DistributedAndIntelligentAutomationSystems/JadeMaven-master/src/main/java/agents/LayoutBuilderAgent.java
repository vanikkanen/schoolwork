/*****************************************************************
 JADE - Java Agent DEvelopment Framework is a framework to develop
 multi-agent systems in compliance with the FIPA specifications.
 Copyright (C) 2000 CSELT S.p.A.

 GNU Lesser General Public License

 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Lesser General Public
 License as published by the Free Software Foundation,
 version 2.1 of the License.


 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public
 License along with this library; if not, write to the
 Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 Boston, MA  02111-1307, USA.
 *****************************************************************/

package agents;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.domain.DFService;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import jade.domain.FIPAException;
import jade.lang.acl.ACLMessage;
import jade.util.Logger;
//Create agents systematically
import jade.wrapper.ContainerController;
import jade.wrapper.StaleProxyException;
import jade.wrapper.AgentController;
import java.util.*;

/**
 * This agent implements a simple Ping Agent that registers itself with the DF and
 * then waits for ACLMessages.
 * If  a REQUEST message is received containing the string "ping" within the content
 * then it replies with an INFORM message whose content will be the string "pong".
 *
 * @author Tiziana Trucco - CSELT S.p.A.
 * @version  $Date: 2010-04-08 13:08:55 +0200 (gio, 08 apr 2010) $ $Revision: 6297 $
 */
public class LayoutBuilderAgent extends Agent{

    private HashMap<Integer, Object[]> convLayout = new HashMap<>();

    private Logger myLogger = Logger.getMyLogger(getClass().getName());

    private class WaitPingAndReplyBehaviour extends CyclicBehaviour {

        public WaitPingAndReplyBehaviour(Agent a) {
            super(a);
        }

        public void action() {
            ACLMessage  msg = myAgent.receive();
            if(msg != null){
                ACLMessage reply = msg.createReply();

                if(msg.getPerformative()== ACLMessage.REQUEST){
                    String content = msg.getContent();
                    if ((content != null) && (content.indexOf("ping") != -1)){
                        myLogger.log(Logger.INFO, "Agent "+getLocalName()+" - Received PING Request from "+msg.getSender().getLocalName());
                        reply.setPerformative(ACLMessage.INFORM);
                        reply.setContent("pung");
                    }
                    else{
                        myLogger.log(Logger.INFO, "Agent "+getLocalName()+" - Unexpected request ["+content+"] received from "+msg.getSender().getLocalName());
                        reply.setPerformative(ACLMessage.REFUSE);
                        reply.setContent("( UnexpectedContent ("+content+"))");
                    }

                }
                else {
                    myLogger.log(Logger.INFO, "Agent "+getLocalName()+" - Unexpected message ["+ACLMessage.getPerformative(msg.getPerformative())+"] received from "+msg.getSender().getLocalName());
                    reply.setPerformative(ACLMessage.NOT_UNDERSTOOD);
                    reply.setContent("( (Unexpected-act "+ACLMessage.getPerformative(msg.getPerformative())+") )");
                }
                send(reply);
            }
            else {
                block();
            }
        }
    } // END of inner class WaitPingAndReplyBehaviour


    protected void setup() {
        // Registration with the DF
        DFAgentDescription dfd = new DFAgentDescription();
        ServiceDescription sd = new ServiceDescription();
        sd.setType("LayoutBuilderAgent");
        sd.setName(getName());
        sd.setOwnership("TILAB");
        dfd.setName(getAID());
        dfd.addServices(sd);

        ContainerController cc = getContainerController();
        AgentController t1 = null;
        //t1 = cc.createNewAgent("MARIO", "agents.ConveyorAgent", new Object[] {"Conveyor4","Conveyor13"});

        convLayout.put(1, new Object[] {"CONV02"});
        convLayout.put(2, new Object[] {"CONV03"});
        convLayout.put(3, new Object[] {"CONV04", "CONV13"});
        convLayout.put(4, new Object[] {"CONV05"});
        convLayout.put(5, new Object[] {"CONV06"});
        convLayout.put(6, new Object[] {"CONV07"});
        convLayout.put(7, new Object[] {"CONV08"});
        convLayout.put(8, new Object[] {"CONV09", "CONV14"});
        convLayout.put(9, new Object[] {"CONV10"});
        convLayout.put(10, new Object[] {"CONV11"});
        convLayout.put(11, new Object[] {"CONV12"});
        convLayout.put(12, new Object[] {"CONV01"});
        convLayout.put(13, new Object[] {"CONV14", "CONV09"});
        convLayout.put(14, new Object[] {"CONV12"});


        try {
            for (int i = 1; i < 15; i++) {
                String index;
                if (i < 10){
                    index = "0" + i;
                }
                else {
                    index = Integer.toString(i);
                }
                t1 = cc.createNewAgent( "CONV" + index, "agents.ConveyorAgent", convLayout.get(i));
                t1.start();
            }

            DFService.register(this,dfd);
            WaitPingAndReplyBehaviour PingBehaviour = new  WaitPingAndReplyBehaviour(this);
            addBehaviour(PingBehaviour);
        } catch (Exception e) {
            myLogger.log(Logger.SEVERE, "Agent "+getLocalName()+" - Cannot register with DF", e);
            doDelete();
        }
    }
}