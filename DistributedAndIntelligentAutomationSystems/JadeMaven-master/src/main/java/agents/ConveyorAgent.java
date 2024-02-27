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
import jade.core.AID;
import jade.core.behaviours.CyclicBehaviour;
import jade.core.behaviours.WakerBehaviour;
import jade.domain.DFService;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import jade.domain.FIPAException;
import jade.lang.acl.ACLMessage;
import jade.util.Logger;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

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
public class ConveyorAgent extends Agent{

    private List<String> SHORTEST_PATH = new ArrayList<>();
    private  Boolean FIRST = true;
    public Object [] args;
    private HashMap<String, String> neighbours = new HashMap<>();
    private ArrayList<String> alive_neighbors = new ArrayList<>();
    private String state = "IDLE";
    private Logger myLogger = Logger.getMyLogger(getClass().getName());
    private int transfer_time = 6000;

    void find_path(Agent myAgent, String dest, AID... to_remove) {
        JSONObject next_json = new JSONObject();
        next_json.put("src", getLocalName());
        next_json.put("midpoints", new JSONArray());
        next_json.put("dest", dest);
        ACLMessage next_msg = new ACLMessage(ACLMessage.CFP);
        next_msg.setContent(next_json.toString());
        List<String> neighbour_list = new ArrayList<>(neighbours.keySet());
        for (int i = 0; i < neighbour_list.size(); i++) {
            AID agentID = new AID((String) neighbour_list.get(i), AID.ISLOCALNAME);

            ACLMessage state_msg = new ACLMessage(ACLMessage.REQUEST);
            state_msg.addReceiver(agentID);
            state_msg.setContent("{\"get_state\": \" \"}");
            myAgent.send(state_msg);

            addBehaviour(new WakerBehaviour(myAgent, 10) {
                protected void handleElapsedTimeout() {
                    if (!Objects.equals(neighbours.get(agentID.getLocalName()), "DOWN")) {
                        next_msg.addReceiver(agentID);
                    }
                }
            });
        }

        addBehaviour(new WakerBehaviour(myAgent, 50) {
            protected void handleElapsedTimeout() {
                if (to_remove.length > 0) {
                    next_msg.removeReceiver(to_remove[0]);
                }
                myAgent.send(next_msg);
            }
        });
    }

    void transfer_pallet(JSONObject pallet, Agent myAgent) {
        if (!Objects.equals(state, "IDLE")) {
            //myLogger.log(Logger.INFO, "  Pallet at " + getLocalName());
            JSONArray midpoints = (JSONArray) pallet.get("midpoints");
            if (!midpoints.isEmpty()) {
                if (midpoints.get(0).equals(getLocalName())) {
                    midpoints.remove(0);
                }
            }
            String next_conv = "";
            if (midpoints.isEmpty()) {
                next_conv = (String) pallet.get("dest");
            } else {
                next_conv = (String) midpoints.get(0);
            }
            String finalNext_conv = next_conv;
            myLogger.log(Logger.INFO, "Pallet at " + getLocalName() + ",  Final destination: " + (String) pallet.get("dest"));
            if ((!Objects.equals((String) pallet.get("dest"), (String) getLocalName()) || !midpoints.isEmpty()) && neighbours.containsKey(finalNext_conv)) {
                addBehaviour(new WakerBehaviour(myAgent, transfer_time) {
                    protected void handleElapsedTimeout() {
                        ACLMessage state_msg = new ACLMessage(ACLMessage.REQUEST);
                        AID agentID = new AID((String) finalNext_conv, AID.ISLOCALNAME);
                        state_msg.addReceiver(agentID);
                        state_msg.setContent("{\"get_state\": \" \"}");
                        alive_neighbors.clear();
                        myAgent.send(state_msg);
                        addBehaviour(new WakerBehaviour(myAgent, 10) {
                            protected void handleElapsedTimeout() {
                                if (Objects.equals(neighbours.get(agentID.getLocalName()), "IDLE") && alive_neighbors.contains(agentID.getLocalName())) {
                                    state = "IDLE";
                                    ACLMessage next_msg = new ACLMessage(ACLMessage.INFORM);
                                    AID agentID = new AID((String) finalNext_conv, AID.ISLOCALNAME);
                                    next_msg.addReceiver(agentID);
                                    next_msg.setContent(pallet.toString());
                                    myAgent.send(next_msg);
                                } else if (!alive_neighbors.contains(agentID.getLocalName())) {
                                    neighbours.remove(agentID.getLocalName());
                                    find_path(myAgent, (String) pallet.get("dest"));
                                } else {
                                    addBehaviour(new WakerBehaviour(myAgent, 5000) {
                                        protected void handleElapsedTimeout() {
                                            ACLMessage check_msg = new ACLMessage(ACLMessage.REQUEST);
                                            AID agentID = new AID((String) finalNext_conv, AID.ISLOCALNAME);
                                            check_msg.addReceiver(agentID);
                                            check_msg.setContent("{\"get_state\": \" \"}");
                                            myAgent.send(check_msg);
                                            addBehaviour(new WakerBehaviour(myAgent, 10) {
                                                protected void handleElapsedTimeout() {
                                                    if (!alive_neighbors.contains(agentID.getLocalName()) || !Objects.equals(neighbours.get(agentID.getLocalName()), "IDLE")) {
                                                        if (!Objects.equals(neighbours.get(finalNext_conv), "BUSY") && (neighbours.keySet().size() > 1)) {
                                                            find_path(myAgent, (String) pallet.get("dest"), agentID);
                                                        } else {
                                                            transfer_pallet(pallet, myAgent);
                                                        }
                                                    } else {
                                                        ACLMessage next_msg = new ACLMessage(ACLMessage.INFORM);
                                                        AID agentID = new AID((String) finalNext_conv, AID.ISLOCALNAME);
                                                        next_msg.addReceiver(agentID);
                                                        next_msg.setContent(pallet.toString());
                                                        myAgent.send(next_msg);
                                                        state = "IDLE";
                                                    }
                                                }
                                            });
                                        }
                                    });
                                }
                            }
                        });
                    }
                });


            } else if (Objects.equals((String) pallet.get("dest"), (String) getLocalName())) {
                myLogger.log(Logger.INFO, "  Pallet at destination " + getLocalName());
            } else {
                myLogger.log(Logger.INFO, "  Route not possible");
            }
        }
    }


    private class ConveyorBehaviour extends CyclicBehaviour {

        public ConveyorBehaviour(Agent a) {
            super(a);
        }

        public void action() {
            ACLMessage  msg = myAgent.receive();
            if(msg != null){
                ACLMessage reply = msg.createReply();
                if(msg.getPerformative()== ACLMessage.CFP){
                    String content = msg.getContent();
                    if ((content != null) ){
                        reply.setPerformative(ACLMessage.INFORM);

                        //Parse JSON
                        JSONParser parser = new JSONParser();
                        try {
                            JSONObject json = (JSONObject) parser.parse(content);
                            String name = (String) json.get("dest");
                            List midpoints = (List) json.get("midpoints");
                            if (!Objects.equals(name, getLocalName()) && !midpoints.contains(getLocalName())) {
                                midpoints.add(getLocalName());
                                json.put("midpoints", midpoints);
                                ACLMessage next_msg = new ACLMessage(ACLMessage.CFP);
                                List<String> neighbour_list = new ArrayList<>(neighbours.keySet());
                                for (int i = 0; i < neighbour_list.size(); i++) {
                                    AID agentID = new AID((String) neighbour_list.get(i), AID.ISLOCALNAME);

                                    ACLMessage state_msg = new ACLMessage(ACLMessage.REQUEST);
                                    state_msg.addReceiver(agentID);
                                    state_msg.setContent("{\"get_state\": \" \"}");
                                    myAgent.send(state_msg);

                                    addBehaviour(new WakerBehaviour(myAgent, 10) {
                                        protected void handleElapsedTimeout() {
                                            if (!Objects.equals(neighbours.get(agentID.getLocalName()), "DOWN")) {
                                                next_msg.addReceiver(agentID);
                                            }
                                        }
                                    });
                                }
                                addBehaviour(new WakerBehaviour(myAgent, 50) {
                                    protected void handleElapsedTimeout() {
                                        next_msg.setContent(json.toString());
                                        myAgent.send(next_msg);
                                    }
                                });
                            }

                            else if (Objects.equals(name, getLocalName())) {
                                myLogger.log(Logger.INFO, "Agent "+getLocalName()+" - Found possible path: " + midpoints);

                                ACLMessage path_msg = new ACLMessage(ACLMessage.PROPOSE);
                                String src = (String) json.get("src");
                                AID agentID= new AID((String) src, AID.ISLOCALNAME);
                                path_msg.addReceiver(agentID);
                                path_msg.setContent(json.toString());
                                myAgent.send(path_msg);
                            }

                        } catch (ParseException e) {
                            e.printStackTrace();
                        }
                    }
                    else{
                        myLogger.log(Logger.INFO, "Agent "+getLocalName()+" - Unexpected request ["+content+"] received from "+msg.getSender().getLocalName());
                        reply.setPerformative(ACLMessage.REFUSE);
                        reply.setContent("( UnexpectedContent ("+content+"))");
                        send(reply);
                    }
                }
                else if (msg.getPerformative()== ACLMessage.PROPOSE) {

                    String content = msg.getContent();
                    if ((content != null)) {
                        reply.setPerformative(ACLMessage.INFORM);
                        //Parse JSON
                        JSONParser parser = new JSONParser();

                        try {
                            JSONObject json = (JSONObject) parser.parse(content);
                            List midpoints = (List) json.get("midpoints");

                            if (FIRST || midpoints.size() < SHORTEST_PATH.size()) {
                                SHORTEST_PATH = midpoints;
                            }
                            if (FIRST) {
                                FIRST = false;
                                addBehaviour(new WakerBehaviour(myAgent, 3000) {
                                    protected void handleElapsedTimeout() {

                                        myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Shortest Path: " + SHORTEST_PATH);
                                        FIRST = true;
                                        state = "BUSY";
                                        transfer_pallet(json, myAgent);
                                    }
                                });
                            }
                        } catch (ParseException e) {
                            e.printStackTrace();
                        }
                    }
                }
                else if (msg.getPerformative()== ACLMessage.REQUEST) {

                    String content = msg.getContent();
                    if ((content != null)) {
                        //Parse JSON
                        JSONParser parser = new JSONParser();

                        try {
                            JSONObject json = (JSONObject) parser.parse(content);

                            if (json.containsKey("get_state")) {
                                json.put("get_state", state);
                                reply.setContent(json.toString());
                                reply.setPerformative(ACLMessage.INFORM);
                                myAgent.send(reply);

                            } else if (json.containsKey("dest")) {

                                String dest = (String) json.get("dest");
                                myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Received PATHING Request from " + msg.getSender().getLocalName());
                                if (dest == getLocalName()) {
                                    myLogger.log(Logger.INFO, "Pallet already at destination");
                                    state = "BUSY";
                                }
                                else {
                                    find_path(myAgent, dest);
                                }
                            } else if (json.containsKey("midpoints")) {

                            } else if (json.containsKey("route")) {
                                JSONObject next_json = new JSONObject();

                                JSONArray midpoints = (JSONArray) json.get("route");
                                String dest = (String) midpoints.remove(midpoints.size()-1);

                                next_json.put("src", getLocalName());
                                next_json.put("midpoints", midpoints);
                                next_json.put("dest", dest);

                                myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Received ROUTE Request from " + msg.getSender().getLocalName());
                                state = "BUSY";
                                transfer_pallet(next_json, myAgent);
                            }
                        } catch (ParseException e) {
                            e.printStackTrace();
                        }
                    }
                }
                else if (msg.getPerformative()== ACLMessage.INFORM) {

                    String content = msg.getContent();
                    if ((content != null)) {
                        //myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Received PING Request from " + msg.getSender().getLocalName());
                        //Parse JSON
                        JSONParser parser = new JSONParser();
                        try {
                            JSONObject json = (JSONObject) parser.parse(content);

                            if (json.containsKey("set_state")) {
                                state = (String) json.get("set_state");
                                myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Received SET_STATE Inform. New State: " + state);
                            } else if (json.containsKey("get_state")) {
                                alive_neighbors.add(msg.getSender().getLocalName());
                                neighbours.put(msg.getSender().getLocalName(), (String) json.get("get_state"));
                            } else if (json.containsKey("transfer_time")){
                                transfer_time = Integer.valueOf((String) json.get("transfer_time"));
                                myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Received TRANSFER_TIME Inform. New transfer time: " + transfer_time);
                            } else if (json.containsKey("midpoints")) {
                                state = "BUSY";
                                transfer_pallet(json, myAgent);
                            } else if (json.containsKey("neighbor")) {
                                neighbours.put((String) json.get("neighbor"), "IDLE");
                                myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Received NEIGHBOR Inform.");
                                myLogger.log(Logger.INFO, "Added neighbor"  + (String) json.get("neighbor") + " to " + getLocalName());
                                myLogger.log(Logger.INFO, getLocalName() + " neighbors: " + neighbours.keySet());

                            } else if (json.containsKey("remove_neighbor")){
                                if (neighbours.remove((String) json.get("remove_neighbor"))!= null){
                                    myLogger.log(Logger.INFO, "Agent " + getLocalName() + " - Received REMOVE_NEIGHBOR Inform.");
                                    myLogger.log(Logger.INFO, "Removed neighbor " + (String) json.get("remove_neighbor") + " from " + getLocalName());
                                }
                                myLogger.log(Logger.INFO, getLocalName() + " neighbors: " + neighbours.keySet());

                            }

                        } catch (ParseException e) {
                            e.printStackTrace();
                        }
                    }
                }

                else {
                    //myLogger.log(Logger.INFO, "Agent "+getLocalName()+" - Unexpected message ["+ACLMessage.getPerformative(msg.getPerformative())+"] received from "+msg.getSender().getLocalName());
                    reply.setPerformative(ACLMessage.NOT_UNDERSTOOD);
                    reply.setContent("( (Unexpected-act "+ACLMessage.getPerformative(msg.getPerformative())+") )");
                    send(reply);
                }

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
        sd.setType("ConveyorAgent");
        sd.setName(getName());
        sd.setOwnership("TILAB");
        dfd.setName(getAID());
        dfd.addServices(sd);

        args = getArguments();
        for(Object obj : args){
            neighbours.put((String) obj, "IDLE");
        }
        myLogger.log(Logger.INFO, getLocalName()+" My neighbours are: "+neighbours.keySet());

        try {
            DFService.register(this,dfd);
            ConveyorBehaviour newBehaviour = new  ConveyorBehaviour(this);
            addBehaviour(newBehaviour);
        } catch (FIPAException e) {
            myLogger.log(Logger.SEVERE, "Agent "+getLocalName()+" - Cannot register with DF", e);
            doDelete();
        }
    }
}
