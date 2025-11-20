#### AI agent planning

  #### Gen AI, an AI agent

  

Remember, in module number nine, we explored the concept of an **LLM-powered AI agent**

We defined

_The LLM-powered AI agent system_ **_relies on LLM to function as its brain_**_, which is supported by several crucial components that deploy various important functions._

Let us look at how Gen AI–enabled agents can ease the automation of complex and open-ended use cases:

##### 1- Agents can manage multiplicity

  

Many business use cases and processes are characterized by a linear workflow, with a clear beginning and a series of steps that lead to a specific resolution or outcome.

This relative simplicity makes them easily codified and automated in rule-based systems.

But rule-based systems often exhibit “brittleness”—that is, they break down when faced with situations not contemplated by the designers of the explicit rules.

Many workflows, for example, are far less predictable, marked by unexpected twists and turns and a range of possible outcomes; these workflows require special handling and nuanced judgment that makes rules-based automation challenging.

But gen AI agent systems, because they are based on **foundation models**, have the potential to handle a wide variety of less-likely situations for a given use case, adapting in real time to perform the specialized tasks required to bring a process to completion.

##### 2- Agent systems can be directed with natural language.

  

Currently, to automate a use case, it must first be broken down into a series of rules and steps that can be codified.

These steps are typically translated into computer code and integrated into software systems—an often costly and laborious process that requires significant technical expertise.

Because agentic systems use natural language as a form of instruction, even complex workflows can be encoded more quickly and easily.

What’s more, the process can potentially be done by **nontechnical employees**, rather than software engineers.

This makes it easier to integrate **subject matter expertise**, grants wider access to gen AI and AI tools, and eases collaboration between technical and nontechnical teams. 

##### 3- Agents can work with existing software tools and platforms.

  

In addition to analyzing and generating knowledge, agent systems can use **tools and communicate across a broader digital ecosystem.**

For example, an agent can be directed to work with software applications (such as plotting and charting tools), search the web for information, collect and compile human feedback, and even leverage additional foundation models.

Digital tool use is both a defining characteristic of agents (it’s one way that they can act in the world), but also a way in which their gen AI capabilities can uniquely be brought to bear.

**Foundation models** can learn how to interface with tools, whether through natural language or other interfaces.

**Without foundation models**, these capabilities would require extensive manual efforts to integrate systems (for example, using extract, transform, and load tools) or tedious manual efforts to collate outputs from different software systems.

---

Have a look at the diagram below, prepared by McKinsey& Company:

  

![Agent and Gen AI](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327322-dt-content-rid-27641055_1/xid-27641055_1)

  

Generative AI is transforming the development of intelligent agents by enhancing **learning efficiency, improving their understanding of environments, and enabling more complex interactions through generative models**.

  

![references banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327322-dt-content-rid-27641058_1/xid-27641058_1)

  

- Chapters 3: “Building Agentic AI Systems”, 2025, by Anjanava Biswas and Wrick Talukdar, published by Packt Publishing.
- McKinsey Digital Practice: Why agents are the next frontier of generative AI  By Lareina Yee, Michael Chui, and Roger Robert with Stephen Xu

Now that we have covered AI agents’ **knowledge** and how they represent knowledge. In addition to how they can **reason** using techniques such as deductive, inductive, and abductive reasoning, they can also **adapt** using techniques such as supervised learning, unsupervised learning, reinforcement learning, and transfer learning.

Intelligent agents need to start putting all these core concepts together by making a **plan** to achieve **a goal**.

As noted from the figure below, **reasoning** and **planning** come hand in hand.

Also, a plan is divided into **actions**, and sometimes we call them **tasks**.

![Intelligent agent reasoning and planning](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-27641042_1/xid-27641042_1)

  

  

_But does the agent always get the plan right from the first time???_

_Well, not really, and here comes the concept of adaptability and reiteration._

#### Planning algorithms

  

_Let us start by asking what is a planning algorithm????_

_A planning algorithm derives sequences of actions for an agent to take in order to achieve its_ **_goals_** _from a given_ **_initial state_**

Well, the good news you already know some of them from COMP 237 😊

Some of the most common planning approaches are:

1. Graph-based planning
2. Heuristic search
3. Monte Carlo tree search (MCTS)
4. Hierarchical planning
5. Constraint satisfaction

Let us explore each further.

##### 1- Graph-based planning

  

Graph-based planning represents a planning problem as a **graph**, where the nodes correspond to **possible states** or configurations, and the edges represent actions or transitions that can be taken to move between states.

A fundamental concept within graph-based planning algorithms is the **state-space graph,** which is a graph representation where nodes represent all possible states in the problem domain.

In such a representation, the edges represent the actions or transitions between the states.

This graph representation effectively maps out the entire “space” of possible situations and how they connect with each other via edges.

An edge cost is a property of an edge in a weighted graph. Each edge can have an associated cost (or weight) that represents some measure of the “expense” of taking that action or making that transition.

**Costs** could represent factors such as distance, time, energy consumption, financial cost, or any other relevant metric appropriate for the use case.

Using state-space graphs, edges, and edge costs, there are two broad categories of graph-based planning algorithms:

**1- Graph search:**  Some of the most common algorithms under this category are:

1. Depth-first search (DFS)
2. Breadth-first search (BFS)
3. Dijkstra’s algorithm  (UCS)

**2- Optimal path finding:** Two of the algorithms in this category are:

1. The Bellman-Ford algorithm.
2. The A* search.

The downsides of using graph-based planning algorithms are:

1. We have to include fixing the state representation (state space) upfront.
2. The potential for exponential growth in the number of states to represent and store as problems get more complex.

**Examples** of domains using Graph-based planning techniques are:

1. **Navigation and route planning**, such as GPS systems using graph representations of road networks to find optimal routes, minimizing travel time or distance.
2. **Logistics and supply chain** applications involve planning optimal sequences of operations for manufacturing products or finding the least-cost shipping routes and delivery schedules.
3. **AI planning** employs graph-based methods for game AI move sequencing in chess, video games, and real-time strategy games, as well as for task planning in AI assistants.

  

Graph based palnning algorithms

  

![M3_DFS_exp.png](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-1692643_1/xid-1692643_1)

  

Depth-first search (DFS)

![M3_BFS__fringe.png](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-1692647_1/xid-1692647_1)

  

Breadth-first search (BFS)

![M3_UCS.png](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-1692652_1/xid-1692652_1)

  

Dijkstra’s algorithm  (UCS)

![Astar example](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-1692682_1/xid-1692682_1)

  

A star

Images from COMP 237

---

##### 2- Monte Carlo tree search (MCTS)

  

The core idea behind **MCTS** is to **iteratively** build an **asymmetric search tree by running many random simulations** (playouts) from the current state.

An asymmetric tree means that the tree is not balanced or uniform in its structure.

The results of these **simulations are used to guide the growth of the most promising branches** in the tree at each iteration.

We can think of MCTS as a mix of the graph-based approach and reinforcement learning.

Now the fun part

Watch  this video to get a better understanding of MCTS

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-18354_1/xid-18354_1)

  

  

  

  

The key advantages of MCTS are anytime behavior, the ability to handle large action spaces, and reasoning about long-term outcomes through simulations.

---

#### **3-** Hierarchical planning

  

**Hierarchical planning** approaches break down complex problems into hierarchies of higher-level tasks or goals, and subtasks or subgoals that achieve those higher-level objectives.

This hierarchical **decomposition** allows reasoning about problems more **abstractly** and reusing solutions to common subproblems.

The  advantages of hierarchical approaches are:

1. Computational efficiency by reusing subplan solutions and avoiding reasoning about all details simultaneously
2. Knowledge representation at multiple levels of abstraction
3. Increased scalability to handle very complex problems

Let us look at an example:

**Hierarchical Planning in Autonomous Driving**

![car icon](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-27641052_1/xid-27641052_1)

  

  

Hierarchical planning is critical for managing the complexity of autonomous driving. It divides the overall task of driving into different levels, making it easier for the AI system to make decisions efficiently. Here’s how hierarchical planning is structured in autonomous driving:

###### 1. High-Level Goal:

The primary objective for an autonomous vehicle is to safely reach its destination while following traffic regulations and avoiding obstacles.

###### 2. Major Steps:

- **Route Planning**: At the highest level, the vehicle plans the overall route from the starting point to the destination, considering factors like traffic conditions, shortest distance, and road types.
- **Path Planning**: The next step involves deciding the specific path within the chosen route, such as lane changes and positioning to avoid obstacles or traffic jams.
- **Behavior Planning**: This level focuses on how the vehicle should respond to specific scenarios, such as stopping at traffic lights, yielding to pedestrians, or overtaking other vehicles.
- **Motion Planning**: This involves real-time movement control, such as steering, acceleration, and braking, based on immediate environmental changes.

###### 3. Minor Steps (Sub-divisions within Major Steps):

- **Route Planning**:
- **Road Type Selection**: Choosing whether to take highways, local roads, or detours based on speed and safety.
- **Path Planning**:
- **Lane Management**: Deciding the most appropriate lane to stay in or switch to based on traffic flow and destination proximity.
- **Behavior Planning**:
- **Signal Recognition**: Detecting traffic signals and adjusting behavior, like stopping or slowing down at intersections.
- **Motion Planning**:
- **Obstacle Avoidance**: Making small adjustments to the vehicle’s path to avoid pedestrians, vehicles, or other obstacles detected in real-time.

---

#### 4- Constraint satisfaction

  

**Constraint satisfaction problems (CSPs)** involve formulating the problem as a set of constraints that must be satisfied, and then using **constraint propagation techniques** to eliminate inconsistent possibilities from the search space.

 This process helps reduce the search space by narrowing down the possible values for each variable, making the search for solutions more efficient.

It is important in areas such as **scheduling, planning**, and **resource allocation**.

Let us try to understand with this simple example:

Consider two variables X and Y, each with the domain {1, 2, 3}, and the constraint is that X and Y must not have the same value.

- **Step 1:** Initially, both X and Y have the domain {1, 2, 3}.
- **Step 2:** If X is assigned the value 1, the constraint X ≠ Y implies that Y cannot be 1. Therefore, Y’s domain is reduced to {2, 3}.
- **Step 3:** Now, if Y is assigned the value 2, the constraint X ≠ Y tells us that X cannot be 2. So, X’s domain is reduced to {1, 3}.
- **Step 4:** This process continues with further assignments, but once no more values can be eliminated, we have reached a stable state.

At this point, the domains of X and Y are reduced, and the remaining possible values for each variable make it easier to find a valid solution that satisfies the constraints.

In COMP 247, we will learn about support vector machines, and you will experience further constraints.

---

#### Utility Functions for decision making

  

A utility function quantifies an agent’s preferences by mapping outcomes to utility values, enabling the agent to compare and choose actions that maximize expected utility. Utility functions play a central role in decision-making for intelligent agents by providing a quantitative way to represent and reason about preferences over different outcomes or states of the world.

We will cover this with an example in the lab.

  

![references banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327321-dt-content-rid-27641053_1/xid-27641053_1)

  

- Chapters 3: “Building Agentic AI Systems”, 2025, by Anjanava Biswas and Wrick Talukdar, published by Packt Publishing.
- AI and Games: https://www.youtube.com/watch?v=lhFXKNyA0QA
- Applied roots: [https://www.appliedaicourse.com/blog/hierarchical-planning-in-artificial-intelligence/](https://www.appliedaicourse.com/blog/hierarchical-planning-in-artificial-intelligence/)
- Geeks for Geeks: [https://www.geeksforgeeks.org/artificial-intelligence/constraint-propagation-in-ai/](https://www.geeksforgeeks.org/artificial-intelligence/constraint-propagation-in-ai/)
# Discuss reasoning techniques and learning mechanisms for intelligent agents

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-18323_1/xid-18323_1)

####   

#### Reasoning mechanisms in intelligent agents

  

Once an intelligent agent has a robust way to **represent its knowledge**, reasoning mechanisms allow it to **intelligently manipulate** and **make use** of that information. **Reasoning capabilities** enable agents to:

1. Derive new insights
2. Draw logical conclusions
3. Explain observations
4. Make informed decisions to achieve their goals.

![Reasoning](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-27641042_1/xid-27641042_1)

  

  

  

Important

Reasoning in intelligent agents is rarely a singular, monolithic process.

Sophisticated agent architectures tend to employ a **multi-faceted** reasoning approach that **combines different reasoning styles and data-driven, analytical, and learned components.**

##### Reasoning paradigms

There are three well-known paradigms:

 1- Deductive

2-  Inductive

3- Abductive reasoning

Let us explore each of these paradigms:

#### 1- Deductive reasoning

  

**Deductive reasoning** is a fundamental form of logical reasoning that follows a **top-down approach.**

In deductive reasoning, an intelligent agent starts with general premises or rules about a domain and applies them to derive specific, logically inescapable conclusions.

**Example:**

“All men are mortal.

Socrates is a man.

Therefore, Socrates is mortal.”

If the initial premises (“All men are mortal” and “Socrates is a man”) are true, then the conclusion “Socrates is mortal” follows inescapably from applying the rules of deductive logic. 

Have a look at the figure on the left. Deductive reasoning follows the path:

from **general premises** to **specific conclusions**

**It is a form of validating a hypothesis.**

  

  

![deductive reasoning](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-27641045_1/xid-27641045_1)

  

  

 Deductive reasoning

**Deductive reasoning** is particularly powerful when combined with other forms of reasoning, such as **abduction** or **induction**.

Example:

Abduce possible disease hypotheses from symptoms (inference to the best explanation)

Deduce expected findings for each hypothesis using rules about disease models

Compare deduced findings to actual patient data to confirm/reject hypotheses

- Deduction alone cannot acquire entirely new knowledge.
- Deduction is indispensable for intelligent agents to logically expand their knowledge.
- Deduction enforces consistency and enables rational decision-making.
- Deductive reasoning provides the rigor to ensure the trustworthiness of an agent’s conclusions.

**Deductive reasoning** finds application across many domains, such as these:

**Mathematics/geometry:** Formal mathematical proofs are quintessential examples of deductive reasoning, deriving specific theorems from general axioms and previously proven statements

**Law:** Legal reasoning applies codified laws and precedents to derive judgments about particular cases through deduction

**Software verification:** Formal verification techniques use deductive reasoning over logical specifications to prove correctness properties of hardware/software systems

**Network routing:** Routing protocols determine optimal paths by deductively applying rules/constraints about network topology, bandwidth, and so on

Fun time 😊

Let us watch the video below, then carry out the activity:

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-18354_1/xid-18354_1)

  

  

  

  

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-18302_1/xid-18302_1)

  

After watching the video, what are the main points for deductive reasoning to succeed?

It works well combined with inductive reasoning.

It needs good rules and data to start with; otherwise, garbage in, garbage out applies.

It requires complicated numeric math.

---

#### **2- Inductive reasoning**

  

**Inductive reasoning** follows a **bottom-up** methodology.

Inductive reasoning involves **making generalizations** or deriving probable conclusions from a set of **specific observations or data points**.

**Example:**

“The Sun has risen every day for the past million days.

Therefore, the sun will likely rise again tomorrow.”

Based on the repeated instances of the sun rising, an inductive reasoning process allows an intelligent agent to hypothesize or induce that the sun will continue rising in the future.

  

![Inductive reasoning](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-27641046_1/xid-27641046_1)

  

Inductive reasoning

**Inductive reasoning** has immense applicability in the following real-world domains:

1. **Scientific method:** The process of formulating scientific laws/theories relies heavily on inductively generalizing from experimental observations and data.
2. **Machine learning:** ML algorithms essentially perform inductive reasoning, inferring general models from training data that can make predictions on new instances.
3. **Pattern recognition:** Computer vision, signal processing, and other pattern recognition tasks use inductive techniques to classify inputs based on detected statistical regularities.
4. **Data mining:** Approaches such as association rule mining inductively identify frequently occurring patterns, correlations, or relationships in large datasets.
5. **Natural language acquisition:** Children learn grammar rules and language models through inductive generalization from the linguistic inputs they receive.

**Important**

**Inductive conclusions are not logically guaranteed to be true – they merely suggest a likely possibility based on the observed evidence.** 

  

**Inductive reasoning** is indispensable for intelligent agents operating in **noisy, uncertain environments** where **knowledge is not fully available upfront**.

Again, it is powerful when combined with other forms of reasoning.

---

#### 3- **Abductive reasoning**

  

**Abductive reasoning** is a form of reasoning that works **backward** – attempting to find the most **plausible explanations** or premises that could account for a given set of observations or data.

 Also known as:

**Inference to the best explanation**

**Example:**

“The lawn is wet.

A plausible explanation: It rained last night.”

**Abductive reasoning** allows an **intelligent agent** to rationally deduce or infer that the most likely explanation, based on past experience, is that it rained the previous night, even though **that was not directly observed**.

  

![Abductive reasoning](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-27641047_1/xid-27641047_1)

  

Abductive reasoning

###### **Abductive reasoning** facilitates thinking outside the box and exploring novel possible explanations.

  

###### The advantage of abductive reasoning:

  

**Abductive reasoning** has the ability to generate **new plausible premises** that **deductive or inductive methods cannot produce** solely from existing knowledge and data.

Having said that:

Implementing abductive reasoning in agentic systems is **challenging** due to its **computational complexity**, as generating and evaluating **multiple hypotheses** can be **resource-intensive**.

**Abductive reasoning** is extremely useful in diagnostic domains and applications where **root cause analysis is critical,** for example, these cases:

1. **Medical diagnosis:** Given a set of symptoms, physicians abduce and investigate the most probable diseases or conditions that could explain those symptoms
2. **Fault detection:** Monitoring systems in manufacturing use abduction to isolate the most likely faults or failures that led to observed anomalies
3. **Forensics/criminal investigation:** From crime scene evidence, detectives abduce possible scenarios and suspect profiles to determine what transpired
4. **AI planning:** For agents to achieve desired goals, they must abduce sequences of viable actions by reasoning backward from those goals
5. **Scientific discovery:** New scientific theories are often initially inferred by finding explanatory hypotheses for currently unexplained observations or phenomena

Fun time 😊

To get the idea better, watch this short video:

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-18354_1/xid-18354_1)

  

  

  

  

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-18303_1/xid-18303_1)

  

The **most creative** form of reasoning is:

Deductive reasoning

Abductive reasoning

Inductive reasoning

The **riskiest** form of reasoning is:

Deductive reasoning

Inductive reasoning

Abductive reasoning

#### Learning mechanisms for adaptive agents

  

Learning mechanisms are key to enabling intelligent agents to adapt to changes in their environment or to improve over time.

The ability to learn allows agents to continuously refine their knowledge and behavior based on new experiences and data.

There are numerous approaches to learning, each with its own strengths and applications:

##### 1- Supervised learning

This learning paradigm involves training an agent on a dataset where the inputs are paired with corresponding labeled outputs or target values. The aim is for the agent to learn a mapping function that accurately predicts outputs for new, unseen inputs.

Supervised learning is widely used for classification and regression tasks across domains such as these:

- Image classification
- Spam detection
- Machine translation
- Medical diagnosis

##### 2- Unsupervised learning:

Here, the agent is trained on unlabeled data without any associated target outputs. The goal is to discover inherent patterns, correlations, or groupings within the data itself in an unsupervised manner. Key applications include the following:

- Customer segmentation
- Anomaly detection
- Topic modeling
- Dimensionality reduction

##### 3 -Reinforcement learning (RL)

This learning approach is inspired by how humans and animals learn – through **trial and error** using feedback from the environment in the form of rewards or punishments. An RL agent learns optimal behaviors/policies by trying out different actions and updating its strategy based on the observed rewards. RL has seen great success in domains such as the following:

- Game playing
- Robotics
- Supply chain optimization
- Traffic signal control

##### 4- Transfer learning:

This technique focuses on transferring knowledge learned in one setting to facilitate learning in a different but related setting. By leveraging previously learned patterns and representations, transfer learning can significantly accelerate training speed and sample efficiency for new tasks. Applications span areas such as the following:

- Natural language processing
- Computer vision
- Recommendation systems

  

These learning mechanisms, often used in hybrid combinations, equip intelligent agents with the ability to continuously expand their knowledge, refine their behaviors, and grow their problem-solving capabilities – the key hallmarks of intelligence. As learning algorithms advance, agents will only become more adaptable and robust when facing new challenges.

Don’t worry for now, we will be covering the algorithms in future courses. 😊

  

![references banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-27641048_1/xid-27641048_1)

  

- Chapters 3: “Building Agentic AI Systems”, 2025, by Anjanava Biswas and Wrick Talukdar, published by Packt Publishing.
- robertus : [https://www.youtube.com/watch?v=Eco5_X17TBU](https://www.youtube.com/watch?v=Eco5_X17TBU)

  

![Footer banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327317-dt-content-rid-27641049_1/xid-27641049_1)


# Explore knowledge representation in intelligent agents

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-18323_1/xid-18323_1)

#### Knowledge representation

  

Remember, in module number nine, we touched on the architecture of intelligent agents. Recall the diagram below for deliberative agents:

![Knowledge of intelligent agents](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-27641034_1/xid-27641034_1)

  

  

  

**The Knowledge base** is key and one of the core functions of intelligent agents, because the knowledge base that stores symbolic representations of:

- The environment
- Goals
- Constraints
- Domain-specific knowledge

_The question is:_

_How do we store such knowledge and in what format??_

_The answer is there any many formats, as below:_

1. _Semantic networks_
2. _Frames_
3. _Logic-based representations_

_Let us explore each:_

#### 1- Semantic networks

  

 Semantic networks are **graph-based** structures composed of **nodes** that represent:

- Concepts
- Entities
- Events
- States in the world.

These **nodes** are connected by **labeled edges** that explicitly define the **semantic relationships** between the represented concepts.

The simplicity yet expressiveness of semantic networks allows them to naturally capture the rich, diverse relationships and interconnections that exist in our complex world.

Have a look at the two diagrams on the left.

Semantic networks gain much of their power from their ability to perform **generalization** through the **inheritance of properties** along **relationship paths**.

_But how would they be able to generalize???_

Let us look at the example of the dog relationships:

If the network specifies that dogs are a subclass of animals and that animals breathe air, then an agent can **semantically infer** that dogs also breathe air through inheritance.  

  

  

  

  

![A semantic knowledge graph for a dog](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-27641037_1/xid-27641037_1)

  

Semantic network representing “Dog” relationships

![Semantic network representing “Disease” relationships](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-27641038_1/xid-27641038_1)

  

Semantic network representing “Disease” relationships

_So, why not store as SQL tables???_

_Well, it would be hard to catch the relationships. Watch this video to get an idea:_

  

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-18354_1/xid-18354_1)

  

  

  

_How can we implement a semantic data model in my AI application?_

To integrate a **semantic data model**, follow these steps:

1. **Define the data ontology** – Identify entities, attributes, and relationships.
2. **Structure the semantic model** – Use frameworks like OWL or RDF.
3. **Build a knowledge graph** – Implement the model in **Neo4j, Amazon Neptune, or another graph database**.

- Semantic networks integrate naturally with other symbolic reasoning techniques.
- Their graph-based structure maps well to deductive methods such as first-order logic, where nodes become constants or predicates and edges become relations that can participate in logical proofs and inference rules.
- An intelligent tutoring system could use this combined representational power for logic-based explanations and teach students new concepts based on their semantic knowledge graphs.

---

#### **2- Frames**

  

The frame knowledge representation paradigm provides a structured way for intelligent agents **to model concepts and their associated attributes**.

Frames provide an intuitive model for representation that **mirrors how humans conceptualize knowledge about the world**.

Their **hierarchical nature** aligns with how people form conceptual abstractions and categorize ideas based on shared attributes and relations.

**Classes** in object-oriented programming (OOP)  languages are essentially frame-like structures encapsulating **attributes and methods**.

  

![Frame example](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-27641039_1/xid-27641039_1)

  

#### 3- **Logic-based representations**

  

The logic-based approach takes a more formal, **mathematical** route.

Logic-based knowledge representation employs the machinery of **symbolic logic** to encode **facts, rules, and axioms about a domain**.

In this paradigm, **statements representing knowledge** are translated into well-formed formulae in formal **logical languages** such as:

1. Propositional logic.
2. First-order logic.
3. Temporal logic.
4. specialized modal/temporal logics. 

Let us have a look at some **examples**:

###### First-order logic

**“All humans are mortal”** can be represented as **∀x** **(Human(x) → Mortal(x))**

**∀x**: Universal quantifier meaning “_for all x_.”

###### Propositional logic

**“It is raining or it is sunny”** can be expressed as **Rain** **∨** **Sunny**

**∨** : Logical disjunction meaning “or.”

###### Temporal logic

**“Eventually, the system will stabilize”** can be **modeled as** ◇ **Stable**

**◇**: Diamond operator in temporal logic meaning “eventually.”

These logical formulae act as the building blocks for constructing a comprehensive knowledge base using strict logical deductive systems with clearly defined axioms, inference rules, and formal semantics.

An **inference engine** can then derive new facts and conclusions from the existing knowledge by applying the rules of logical reasoning.

Sounds complicated :(  Watch this video to get a better idea about propositional logic:

  

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-18354_1/xid-18354_1)

  

  

  

  

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-18302_1/xid-18302_1)

  

During the video, the concept of **truth tables** has come up in propositional logic

1. What do you think of truth tables?
2. Do they make sense?
3. Think about what could be a disadvantage of truth tables?

###### Advantages of logic-based representation:

  

- A key advantage of logic-based representations is their formal rigor and associated strong theoretical properties.
- Systems built on logical foundations can provide guarantees around soundness (only deriving logically valid conclusions) and completeness (deriving all possible valid conclusions).
- This mathematical grounding makes logic attractive for knowledge representation in safety-critical domains. 

  

![references banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327316-dt-content-rid-27641040_1/xid-27641040_1)

  

- Chapters 3: “Building Agentic AI Systems”, 2025, by Anjanava Biswas and Wrick Talukdar, published by Packt Publishing.
- appsmith_ : [https://www.appsmith.com/blog/semantic-data-model-blind-spot-ai-agents](https://www.appsmith.com/blog/semantic-data-model-blind-spot-ai-agents)
- Spanning Tree: [https://www.youtube.com/watch?v=5NGKbiA04Cw](https://www.youtube.com/watch?v=5NGKbiA04Cw)


**Lab1: Travel Booking Assistant Flowchart with Agency and Autonomy** 

Prepared by: Professor Vaishali Chandrashekar Siddeshwar

  

This lab demonstrates the concepts of Agency and Autonomy using the Travel Booking Assistant example.

  

**Flowchart: Travel booking assistant**

In the code, the book_travel function takes a departure city code (such as SAN or SEA, which are airport codes) and subsequently calls other functions to set the goal, update its knowledge base, and then make a decision on which flight to choose and book that flight. 

![FlowChart of Travel Assistant Agent](https://luminate.centennialcollege.ca/bbcswebdav/pid-4336179-dt-content-rid-27896337_1/xid-27896337_1)

**Source Code**

Download the script below, and examine it.

Week9_lab1_AgencyAutonomy_Demo.zip

  

**Libraries Needed**

Ensure that you have the following libraries installed in your Anaconda environment.

1. faker

  

If not, search for "Anaconda Prompt" in your Search and open it. Execute the following command to install the library.

pip install faker

**Sample Output**

The output of this code when the agent is initialized to book a flight from SAN (San Diego) to SEA (Seattle) looks as follows:

![Week9_lab1 example output](https://luminate.centennialcollege.ca/bbcswebdav/pid-4336179-dt-content-rid-27896341_1/xid-27896341_1)

  

**Drawbacks of The Agent**

- Note that our Agent has some functionality of agency and autonomy, but is not intelligent. 
- It requires discrete inputs, specifically airport codes - the departure city code and the arrival city code - to operate.
- However, it cannot infer what the user intends to do to set its goals, update its knowledge base, and then perform the actions if the input text is plain language, such as “_Book me a flight from San Diego to Seattle”_.
- This is where generative AI steps in.ulti-agent system example with UML diagrams

  

#### Example:

#### Design a Multi-agent system with a front end

  

The multi-model Travel Planning System is an AI-driven assistant that integrates multiple specialized models to generate personalized travel plans. It consists of four key agents:

WeatherAnalysisAgent: Predicts the best travel months using historical weather data

HotelRecommenderAgent: Uses a transformer model to find accommodations that match user preferences

ItineraryPlannerAgent: Employs GPT-2 to generate detailed day-by-day travel plans

MutliModelTravelPlanning (SummaryAgent): Creates professional trip summaries and cost estimates, communicates with the databases and the other three agents, and the frontend.

The system follows a structured data flow, where the user inputs their destination, preferences, and duration, and the agents collaborate to deliver a complete travel plan.

The core AI models include:

1. RandomForestRegressor for weather predictions
2. SentenceTransformer for hotel recommendations
3. GPT-2 for generating itineraries and summaries.
4. Streamlit is used for the front end.

##### Activity workflow diagram

  

The activity diagram describes the control flow of the application, starting from the collection of user input through to the generation of a complete travel plan. It illustrates how each agent is triggered and how their outputs are merged:

  

![Example activity workflow  diagram travel](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327380-dt-content-rid-27641646_1/xid-27641646_1)

  

Image source: “Building AI Agents with LLMs, RAG, and Knowledge Graphs" by Salvatore Raieli, Gabriele Iuculano

##### Class Diagram illustrating interactions with external Components

  

The class diagram illustrates the primary components of the application, including the core AI agents (such as WeatherAnalysisAgent and ItineraryPlannerAgent), the underlying models (RandomForest, SentenceTransformer, and OpenAI GPT), and the Streamlit app that connects the user interface to the backend logic. Notice the relationships on the dashed lines in the class diagram.

  

![Example  class diagram illustrating interaction with external components](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327380-dt-content-rid-27641649_1/xid-27641649_1)

  

Image source: “Building AI Agents with LLMs, RAG, and Knowledge Graphs" by Salvatore Raieli, Gabriele Iuculano

##### Interaction diagram (Sequence diagram)

  

The sequence diagram outlines the time-based interactions between the Streamlit frontend, the database, and the AI agents. It displays the order of method calls, the data exchanged, and the points at which the system waits for responses. It makes clear when and how each agent is called. Notice at the top the different components and databases.

  

![Example interaction diagram](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327380-dt-content-rid-27641650_1/xid-27641650_1)

  

Image source: “Building AI Agents with LLMs, RAG, and Knowledge Graphs" by Salvatore Raieli, Gabriele Iuculano
# Explain the architecture of agentic systems

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-18323_1/xid-18323_1)

#### **Intelligent (Agentic) architecture**

  

 **Three architectures have emerged recently:**

1. **Deliberative architectures**
2. **Reactive architectures**
3. **Hybrid architectures architectures**

Let us explore each:

  

#### **1- Deliberative architectures:**

  

Also known as **knowledge-based** or **symbolic architectures**.

They follow the concept of **Sense-Plan-Act**

**Sense:** perceive information about the environment.

**Plan:** make a plan of action according to that perception and the knowledge base.

**Act:** execute such plans of action

  

![Sense act plan  architecture](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-27641626_1/xid-27641626_1)

  

These architectures leverage techniques such as:

- Rule-based reasoning
- Constraint satisfaction
- Heuristic search

To **navigate through** intricate **problem spaces** and formulate **appropriate courses of action**.

Have a look at the figure below:

![Deliberative architecture](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-27641629_1/xid-27641629_1)

  

Deliberative architecture of an agentic system

**The Knowledge base** is key here.

The knowledge base that stores symbolic representations of:

- The environment
- Goals
- Constraints
- Domain-specific knowledge

  

![Knowledge base](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-27641630_1/xid-27641630_1)

  

**Advantages:**

- Ability to handle tasks that involve complex reasoning, such as planning, problem-solving, and decision-making.

 **Dis-advantages:**

1- High computational cost associated with maintaining and reasoning over complex knowledge bases, which can limit real-time responsiveness in dynamic environments.

2- The explicit representation of knowledge can be challenging in domains where knowledge is difficult to formalize or constantly evolving.

To address these limitations, **deliberative architectures** are often combined with **reactive** or **behavior-based components in hybrid architectures**, allowing both **complex reasoning** and **rapid response** to environmental changes.

---

#### **2- Reactive architectures:**

  

Also known as **_behavior-based_** or **_stimulus-response_** architectures.

  

They aim to provide **immediate responses** to stimuli from the environment.

Key characteristics:

1. **Speed and responsiveness:** Reactive architectures are designed to react rapidly to changes in the environment. By directly coupling perceptions to actions, they can bypass time-consuming deliberative reasoning processes, enabling swift and timely responses.
2. **Robustness and fault tolerance:** These architectures are generally robust and **less susceptible to noise** or incomplete information. Their simple, standalone nature makes them less prone to catastrophic failures, as individual components or behaviors can compensate for or mitigate the effects of faulty or missing input, especially when used within a deliberative architecture.
3. **Handling uncertainty:** Reactive architectures can effectively handle uncertainty in dynamic environments. Their ability to respond directly to environmental stimuli allows them **to adapt and adjust their actions based on the current situation**, without relying on precise or complete models of the entire world.
4. **Parallel and distributed processing:** Reactive architectures often employ parallel and distributed processing using multiple reactive modules, where multiple modules operate simultaneously and independently. This decentralized approach enables efficient handling of complex tasks and provides inherent scalability and modularity.
5. **Emergence of complex behavior:** Despite the simplicity of individual behaviors or rules, the interaction and coordination of multiple reactive components can lead to the emergence of complex, intelligent-like behavior at the system level.

  

![Reactive architectures](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-27641631_1/xid-27641631_1)

  

##### Disadvantages of reactive architectures

**Lack of long-term planning:** Reactive architectures generally lack the ability to **plan ahead or reason about long-term consequences**. Their focus is on immediate responses to environmental stimuli, making it difficult to pursue complex, multi-step goals or strategies.

**Limited reasoning and abstraction:** These architectures may struggle with tasks that require **abstract reasoning, generalization, or the manipulation of symbolic representations.** They are primarily designed to operate at a lower, stimulus-response level.

**Limited learning capabilities:** Many reactive architectures lack the ability to learn from experience or adapt their behavior over time. Their fixed set of rules or behaviors may not be suitable for dynamic environments or tasks that require **continuous learning and adaptation**.

  

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-18302_1/xid-18302_1)

  

Now that we know the difference between deliberative and reactive architectures, research the following models and try to classify them as either deliberative or reactive:

1. GPT-4 model
2. GPT-5 model
3.  DeepSeek-V2/V3 model

---

#### 3- Hybrid architectures

  

Researchers have recognized the strengths and limitations of both deliberative and reactive architectures, leading to the development of **hybrid architectures** that aim to exploit the advantages of both approaches.

Such hybrid architectures typically employ a layered structure, consisting of the following:

- **A reactive layer** for fast and low-level responses. The reactive layer is responsible for handling real-time interactions with the environment, providing rapid and situationally appropriate responses to external stimuli. This layer is designed to be highly responsive, fault-tolerant, and capable of handling uncertainty, leveraging the strengths of reactive architectures.
- **A deliberative layer** for high-level reasoning and planning. The deliberative layer is dedicated to higher-level reasoning, planning, and decision-making processes. This layer can maintain a more comprehensive representation of the environment, goals, and constraints, enabling it to formulate complex strategies, reason about abstract concepts, and plan long-term courses of action.

#### Common types of Agents

  

As the term “agent” has gained popularity, its meaning has broadened to encompass a wide range of AI-enabled systems, often creating confusion about what truly constitutes an AI agent. The Information categorizes agents into nine practical types, reflecting how these technologies are being applied today:

###### 1-  Business-task agents

These agents automate predefined business workflows, such as UiPath’s robotic process automation, Microsoft Power Automate’s low-code flows, or Zapier’s app integrations. They execute sequences of deterministic actions, typically triggered by events, with minimal contextual reasoning.

###### 2- Conversational agents

This category includes chatbots and customer service agents that engage users through natural language interfaces. They are optimized for dialogue management, intent recognition, and conversational turn-taking, such as virtual assistants embedded in customer support platforms.

###### 3- Research agents

Research agents conduct information gathering, synthesis, and summarization tasks. They scan documents, knowledge bases, or the web to provide structured outputs that assist human analysts. Examples include Perplexity AI and Elicit.

###### 4- Analytics agents

Analytics agents, such as Power BI Copilot or Glean, focus on interpreting structured datasets and generating insights, dashboards, and reports. They often integrate tightly with enterprise data warehouses, enabling users to query complex data in natural language.

###### 5- Developer agents

Tools like Cursor, Windsurf, and GitHub Copilot represent coding agents, which assist developers by generating, refactoring, and explaining code. They integrate deeply into IDE workflows to augment software development productivity.

**6- Domain-specific agents**

These agents are tuned for specialized professional domains, such as legal (Harvey), medical (Hippocratic AI), or finance agents. They combine domain-specific knowledge with structured workflows to deliver targeted, expert-level assistance.

**7- Browser-using agents**

These agents navigate, interact with, extract information from, and take actions on websites without human interaction. As opposed to traditional robotic process automation, which follows prescripted steps, modern browser-using agents combine language understanding, visual perception, and dynamic planning to adapt on the fly.

###### 8- Voice agents

  

Powered by end-to-end speech understanding and generation, these agents are enabling conversational automation in areas like customer service, appointment scheduling, and even real-time order processing.

###### 9- Video agents

These agents present users with avatar-based video responses, combining lip-synced speech, facial expression, and gesture. They’re emerging rapidly in sales, training, customer onboarding, marketing, and virtual presence tools—enabling scalable, personalized video interactions without manual production.

#### Architecture Design Patterns

The architectural design of agent-based systems determines how agents are structured, how they interact with their environment, and how they perform tasks.

There are two main architectures:

1. Single-Agent Architectures
2. Multiagent Architectures: Collaboration, Parallelism, and Coordination

Let us have a look explore each:

##### Single-Agent Architectures

  

Single-agent setups work well in environments where the problem domain is well-defined, tasks are straightforward, and there is no significant need for scaling.

**Examples:**

- Customer service chatbots
- General-purpose assistants
- Code generation agents Like Copilot

Have a look at the below diagram, we are still at the first era which is **task oriented**, but things are moving fast.

  

![Single agent](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-27641632_1/xid-27641632_1)

  

Image source: The Rise and Potential of Large Language Model Based Agents: A Survey by Zhiheng Xi et al.

The LLM-based agents, which can understand human natural language commands and perform everyday tasks , are currently among the most favored and practically valuable agents by users.

This is because they have the potential to enhance task efficiency, alleviate user workload, and promote access for a broader user base. In task-oriented deployment, the agent follows high-level instructions from users, undertaking tasks such as goal decomposition sequence planning of sub-goals , interactive exploration of the environment, until the final objective is achieved.

##### Multiagent Architectures: Collaboration, Parallelism, and Coordination

  

- In multiagent architectures, multiple agents work together to achieve a common goal.
- These agents may operate independently, in parallel, or through coordinated efforts, depending on the nature of the tasks.
- Multiagent systems are often used in complex environments where different aspects of a task need to be managed by **specialized agents** or where **parallel processing** can improve efficiency and scalability.

**Challenges:**

- Coordination and communication
- Increased complexity
- Lower efficiency

Have a look at the figure below:

![multi agent](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327378-dt-content-rid-27641633_1/xid-27641633_1)

Image source: The Rise and Potential of Large Language Model Based Agents: A Survey by Zhiheng Xi et al.

Interaction scenarios for multiple LLM-based agents. In cooperative interaction, agents collaborate in either a **disordered or ordered** manner to achieve shared objectives. In adversarial interaction, agents compete in a **tit-for-tat** fashion to enhance their respective performance.

For now most efforts are focused on ordered interactions.

#### Principles for Building Effective Agentic Systems

1. **Scalability:**  Ensure that agents can handle growing workloads and diverse tasks by utilizing distributed architectures, cloud-based infrastructure, and efficient algorithms that support **parallel processing** and resource optimization. Example: a customer support agent that processes 10 tickets per minute may crash or hang when traffic spikes to 1,000 if not backed by autoscaling infrastructure.
2. **Modularity:** Design agents with independent, interchangeable components connected through clear interfaces. This modular approach simplifies maintenance, promotes flexibility, and facilitates rapid adaptation to new requirements or technologies. Example: a poorly modular agent that hardcodes all its tools in its agent service would require a full redeployment anytime a small addition or modification is needed to a tool.
3. **Continuous learning:** Equip agents with mechanisms to learn from experience, such as in-context learning. Integrate user feedback to refine agent behaviors and maintain performance relevance as tasks evolve. Example: agents that ignore feedback loops may keep making the same mistakes—like misclassifying contract clauses or failing to escalate critical support issues.
4. **Resilience:** Develop robust resilience architectures capable of:
5. gracefully handling errors
6. security threats
7. timeouts.
8. Incorporate comprehensive error handling, stringent security measures, and redundancy to ensure reliable and continuous agent operations. Example: agents without retry or fallback logic may crash entirely when a single API call fails, leaving the user waiting and confused.
9. **Future-proofing:** Build agent systems around open standards and scalable infrastructure, fostering a culture of innovation to adapt quickly to emerging technologies and evolving user expectations. Example: tightly coupling your agent to one proprietary vendor’s prompt format can make switching models painful and limit experimentation.






#### Multi-agent systems (MAS)

  

_What is a Multi-agent system?_

A multi-agent system (MAS) is a system comprising **multiple autonomous agents** that can **interact, collaborate, and cooperate** to achieve **shared goals.**

  

Wow, a lot of fancy words. Don’t worry, we will go over them.

##### Remember that one of the AI agent's characteristics was **Social ability**

  

Social ability is where they interact and cooperate with other agents or humans to achieve common goals that require collaborative effort.

**Example:**

Let’s think of an example of a supply chain.

MASs can be used to optimize supply chain operations by coordinating the activities of different agents representing **suppliers, manufacturers, distributors, and retailers.**

Each agent can make decisions based on its local knowledge and constraints, while collaborating with other agents to ensure efficient resource allocation, inventory management, and transportation planning.

Have a look at the diagram below:

  

![MAS Supply Chain](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327379-dt-content-rid-27641636_1/xid-27641636_1)

  

#### Characteristics of a MAS system:

  

1. **Autonomy**: Agents operate independently, making their own decisions without direct external control.
2. **Interaction:** Agents communicate and coordinate with each other to achieve individual or shared goals.
3. **Adaptability:** The system can dynamically adjust its behavior in response to a changing environment.
4. **Distributed Control:** Decision-making is spread across the agents, avoiding a central point of control.
5. **Scalability:** The system can efficiently accommodate the addition or removal of agents.
6. **Heterogeneity:** Agents can be diverse in their design, capabilities, and purposes.
7. **Decentralized Data:** Information and knowledge are local to each agent, eliminating a central database.

  

![Characteristics of a MAS system](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327379-dt-content-rid-27641639_1/xid-27641639_1)

  

---

#### **Interaction mechanisms in MASs**

  

There are three aspects of interactions:

1. **Coordination**
2. **Collaboration**
3. **Negotiation**

##### 1- **Cooperation**

Cooperation can be defined as agents working together towards a common goal or objective. It is particularly important in situations where no single agent, acting alone, can accomplish the objective.

![MAS Cooperation](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327379-dt-content-rid-27641640_1/xid-27641640_1)

  

**Example:**

A disaster rescue operation, where **multiple drones**, **robotic agents**, and **humans** need to **cooperate and collaborate** to locate **and rescue victims effectively.** 

##### 2-**Coordination**

Deals with managing interdependencies that arise from the actions and activities of agents within the system.

Coordination is essential when agents share resources and have overlapping responsibilities or conflicting actions.

  

![Screenshot 2025-11-02 at 3.32.35 PM.png](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327379-dt-content-rid-27652163_1/xid-27652163_1)

  

  

Coordination mechanisms in MAS may include strategies such as **task scheduling,** **resource allocation management**, and **conflict resolution**.

**Example:**

_In a manufacturing setting, agents representing different robots on production lines may need to coordinate their actions to ensure efficient use of shared resources, prevent interference, and maintain overall production efficiency._

##### 3-**Negotiation**

Negotiation is the process through which agents reach agreements on how to share resources, divide tasks, or resolve conflicts.

It involves agents making offers, counteroffers, and compromises, even when their interests may initially conflict.

![MAS Negotiation](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327379-dt-content-rid-27641641_1/xid-27641641_1)

  

Negotiation mechanisms in MAS enable agents to find mutually beneficial solutions by exchanging proposals, evaluating alternatives, and reaching consensus.

This is particularly useful in situations where agents have limited or conflicting resources, different preferences, or competing goals.

Negotiation can involve various techniques, such as:

- Auctions
- Voting protocols
- Bargaining strategies
- Game-theoretic approaches

depending on the specific requirements and constraints of the problem domain.

---

#### Travel Agent example:

  

For our travel booking assistant example, we will introduce some new functionalities. In addition to booking flights, we now want our system to find hotels at the destination and create an appropriate travel package for the customer. The algorithm for such an MAS system could look like the workflow diagram below:

  

![MAS architecture travel agent example](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327379-dt-content-rid-27641642_1/xid-27641642_1)

  

The first step is to clearly define a set of agents: in this case, a flight agent (Airline agents), a hotel agent, and a travel agency agent.

_A travel agency agent is responsible for creating travel packages based on the best options available_

Also, have a look at the interaction diagram below :

![MAS interaction diagram](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327379-dt-content-rid-27641643_1/xid-27641643_1)

  

_Notice:_

_h__ow each airline and hotel agent independently updates its pricing._

_how the travel agent interacts with multiple airline and hotel agents to compile travel packages._

_It finds appropriate flight schedules and hotel availability in the destination city and subsequently uses that data to create packages._

  

**Cooperation:**

 since all the agents work towards a **common goal** of booking the travel itinerary for the user

  

  

  

**Coordination:**

 since the travel agency agent **needs input** from both the flight agent and the hotel agent to build a travel package, and then subsequently book the best travel package
#### Agentic systems

  

Let us start by asking:    

 **_What does agentic mean?_**

**_Agentic_** refers to someone or something capable of achieving outcomes independently (“functioning like an agent”) or possessing such ability, means, or power (“having agency”). It is especially used with a type of artificial intelligence (AI), often referred to as an AI agent, designed to execute complex tasks autonomously or with little human involvement.

In social sciences, _agentic_ is more specifically used to describe people’s self-assertive behaviors or actions directed towards individual accomplishment, status, and independence.

                                                                                    **[Meriam Webster Dictionary]**

https://www.merriam-webster.com/slang/agentic

![Image generated by AI: Dictionary](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-27641610_1/xid-27641610_1)

Image generated by AI: Dictionary

The captivating aspect of **agentic systems** lies in the intricate **decision-making** processes they employ, which provide valuable insights into how choices are optimized within specific contexts. 

As a person, if you are making decisions, then you are **accountable** and **responsible** for those decisions

  

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-18354_1/xid-18354_1)

  

  

  

  

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-18302_1/xid-18302_1)

  

After watching the video:

1. What are the suggested ways to evaluate agent behaviors?
2. When preparing the test data, what would you need to consider?

Share with the class and the professor you can the conversation tool, before the end of the day.

#### Applications of Agentic Systems

**Robotics:**

In the field of robotics, agentic systems have paved the way for the design and implementation of autonomous robots capable of navigating complex environments, performing intricate tasks, and adapting to changing conditions. These robots, equipped with decision-making capabilities and agency, have found applications in areas such as manufacturing, exploration, search and rescue operations, and healthcare. For instance, robots with agentic behavior can autonomously navigate through disaster zones, assess potential risks, and make decisions to assist in rescue efforts, demonstrating intelligent and adaptive behavior.

  

![Robotics](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-27641613_1/xid-27641613_1)

  

**Artificial Intelligence**:

Agentic systems have been instrumental in the development of intelligent agents and decision support systems.

These systems leverage advanced algorithms, machine learning techniques, and knowledge representation methods to analyze data, reason about complex scenarios, and provide intelligent recommendations or automated decision-making capabilities.

 Agentic AI systems have been applied in domains such as:

- Finance
- Healthcare
- Transportation
- Marketing
- Software engineering

Enabling more efficient and effective decision-making processes.

  

![AI brain](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-27641614_1/xid-27641614_1)

  

**Systems engineering:**

Agentic systems have facilitated the design and implementation of complex, distributed, and adaptive systems.

 These systems often consist of multiple interacting components or subsystems, each exhibiting agentic behavior and decision-making capabilities.

 Such systems are found in areas such as:

- Power grids
- Transportation networks
- Cyber-physical systems

 where intelligent and **autonomous decision-making** is crucial for **efficient operation**, resource allocation, and fault tolerance.

  

![Ruler (Engineering measurement)](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-27641615_1/xid-27641615_1)

  

#### Concepts

  

Central to the idea of agentic systems are the concepts of:

1. Self-governance
2. Agency
3. Autonomy

  

![Autonomy Agency Self-governence](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-27641616_1/xid-27641616_1)

Remember: If an agent is going to make decisions, then the agent is responsible and accountable.

##### 1. Self-governance

  

Self-governance refers to **the ability of a system or entity to govern or control itself autonomously**, without external direction or control.

**Agentic systems**

 **Self-governance** implies that the system can:

Make its own **decisions**

 Set its own **goals**

Regulate its **behavior** 

based on its internal rules, models, and decision-making algorithms.

Agentic systems interact with the **environment or other systems** in a way that is meaningful to them and, through these interactions, become **influenced****.**

_Remember: If an agent is going to make decisions, then the agent is responsible and accountable._

Five aspects of self-governance:

1. **Self-organization**: The ability to organize and structure its own internal processes, resources, and behavior without external intervention
2. **Self-regulation**:    The capability to monitor and adjust its own actions and outputs based on feedback from the environment or internal states, to ensure it operates within desired parameters or constraints
3. **Self-adaptation**: The ability to modify its behavior, strategies, or decision-making processes in response to changes in the environment or its own internal conditions, to achieve its goals more effectively
4. **Self-optimization**: The ability to continuously improve its performance, efficiency, or decision-making capabilities through learning, experience, or evolutionary processes.
5. **Self-determination**: The ability to set its own objectives, priorities, and courses of action based on its internal decision-making processes, without being entirely controlled by external forces.

_But how do Agentic systems implement Self-governance??_

Self-governance in agentic systems is often enabled by the integration of various technologies, frameworks, and methodologies such as **machine learning**, **knowledge representation, reasoning, and decision-making algorithms.**

These allow the system to process information, learn from data and experiences, and make autonomous decisions based on its acquired knowledge and the current context.

##### **2. Agency**

  

Agency is described as the **capability of an individual**, or any other entity, to **act independently** and **make choices**.

Three concepts under agency, as follows:

**1-Decisional authority:**

This refers to the power or ability to act and perform actions according to a chosen alternative or course of action. Systems with agency possess the autonomy to evaluate different options and select the most appropriate action based on their internal decision-making processes, rather than being solely driven by external forces or predetermined rules.

**2- Intentionality**:

Agency implies the existence of intentions, goals, or objectives that guide the actions and behavior of the system. Agentic systems are not merely reactive; they have a sense of purpose and can pursue specific objectives, adjusting their actions and strategies as necessary to achieve those goals.

**3- Responsibility**:

•Agency is closely tied to the concept of responsibility, which is the answerability or accountability for the outcomes and consequences of one’s actions. Systems with agency are considered responsible for their decisions and the impact of their actions on the environment or other entities they interact with.

Let us have a look at the example below of an AI travel booking agent:

![Example of AI agent agency](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-27641617_1/xid-27641617_1)

  

  

  

##### **3. Autonomy**

  

Autonomy is closely related to the concept of agency **but focuses more specifically on the degree of independence** an entity or system possesses. 

Again three aspects of autonomy:

**1- Operational autonomy**:

This refers to the ability of a system to perform a specific task or set of tasks **without direct human intervention or control**. A system with operational autonomy can execute its functions independently, relying on its own internal processes, decision-making algorithms, and environmental sensing capabilities.

**2- Functional autonomy**:

•This aspect of autonomy involves the system’s ability to make choices and take action to achieve set targets or objectives, modulated by the environment or context in which it operates. **Functionally autonomous systems can adapt their behavior and decision-making processes** in response to changing conditions or stimuli, enabling them to pursue their goals more effectively.

**3- Hierarchical autonomy**:

This aspect relates to the **amount of decisional authority or decision-making power awarded to a system within a larger framework or organizational structure.** Systems with higher hierarchical autonomy have greater latitude in making decisions that impact their subsystems or broader operations, while systems with lower hierarchical autonomy may have more constraints or oversight from higher-level entities

So let us have a look at our travel agent example again:

**1- Operational autonomy**:

- Booking flights or hotels
- Managing reminders
- Retrieving travel information 

**2- Functional autonomy**:

- Interpret user commands.
- Adapt to individual preferences
- Make decisions that align with the user’s goals and context.

**3- Hierarchical autonomy**:

Depends on:

- User privacy preferences.
- System’s access to sensitive data and resources. system’s access to sensitive data and resources. 

  

![Example travel agent autonomy](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327371-dt-content-rid-27641618_1/xid-27641618_1)

  

In **AI** and **robotics**, **autonomy i**s a key concept that refers to the extent to which a system can perform tasks and make decisions without the need for continuous human intervention.

**Important: Autonomy in AI and robotic systems does not necessarily imply a complete absence of human oversight or control.**



#### **LLM-powered AI agent**

  

In the previous module, we covered LLMs and the RAG framework. Now we need to talk about a new term, an **LLM-powered AI agent**. 

  

**_What is an_** **_LLM-powered AI agent_****_???_**

_The LLM-powered AI agent system_ **_relies on LLM to function as its brain_**_, which is supported by several crucial components that deploy various important functions._

_These functions include:_

1. _Planning_
2. _Memory_
3. _Tool use_

Have a look at the diagram below:

  

![Components of AI agents](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327370-dt-content-rid-27641603_1/xid-27641603_1)

  

The key components of AI agents were originally defined at https://lilianweng.github.io/posts/2023-06- 23-agent/

  

![sticker suprise](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327370-dt-content-rid-27641606_1/xid-27641606_1)

  

Wow

  

In an **LLM-powered AI (autonomous) agent system,** LLM functions as the agent’s brain, complemented by several key components:

- **Planning**
- Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks.
- Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes, and refine them for future steps, thereby improving the quality of final results.
- **Memory**
- Short-term memory: It would consider all the in-context learning, for example, prompt engineering, as utilizing the short-term memory of the model to learn.
- Long-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, often by leveraging an **external vector store** and fast retrieval.
- **Tool use**
- The agent learns **to call external APIs** for extra information that is missing from the model weights (often hard to change after pre-training), including current information, code execution capability, access to proprietary information sources, and more.

_So how are these different from the traditional agents, the ones we learnt in COMP 237???_

Traditional agents were designed specifically to address certain problems. They primarily relied on predetermined algorithms or rule sets, excelling in tasks they were built for.

Traditional agents often **struggled with generalization** and reasoning when confronted with tasks outside their initial scope.

  

![Sticker agent fails to generalize](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327370-dt-content-rid-27641607_1/xid-27641607_1)

  

**The introduction of Large Language Models (LLMs)** has brought significant changes to **AI agent design**. These agents, trained on the extensive corpus, are not only proficient in understanding and generating natural language but also display **strong generalization abilities.**

This capability allows them to easily integrate with various tools, enhancing their versatility.'

Also, the emergent abilities of Large Language Models show that LLMs are also good at **reasoning, which can help them learn from fault behavior.** 

#### LLM AI-powered applications

  

Have a look at the table below, just to get a feel:

|   |   |   |
|---|---|---|
|**Category**|**Application**|**Description**|
|**Chatbot**|Pi|Inflection’s chatting AI agent is known for its emotional companionship and high emotional intelligence|
|**Game**|Voyager|The first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention|
|**Coding**|GPT Engineer|An AI coding agent that can generate an entire codebase based on a prompt|
|**Design**|Diagram|An AI-powered and automatable design platform|

|   |   |   |
|---|---|---|
|**Research**|||
||ChemCrow|An LLM chemistry agent designed to accomplish tasks across organic synthesis, drug discovery, and materials design|
||Agent|An intelligent agent system that combines multiple large language models for autonomous design, planning, and execution of scientific experiments|

|   |   |   |
|---|---|---|
|**Collaboration**|||
||DialOp|AI assistants collaborating with one or more humans via natural language to help them make complex decisions|
||MindOS|An engine creating autonomous AI agents for users’ professional tasks|
||MetaGPT|A multi-agent framework assigning different roles to GPTs to form a collaborative software entity for complex tasks|
||Multi-GPT|An experimental multi-agent system where multiple “expertGPTs” collaborate to perform a task, and each has its own short and long-term memory and the ability to communicate with each other.|
||Generative Agents|Multiple AI agents for the interactive simulacra of human behavior|

|   |   |   |
|---|---|---|
|**General purpose**|||
||Auto-GPT|An AI agent chaining LLM “thoughts” together to autonomously achieve whatever goal users se|
||BabyAGI|A task-driven autonomous agent leveraging GPT-4 language model, Pinecone vector search, and the LangChain framework to perform a wide range of tasks across diverse domains|
||SuperAGI|A developer-centric open-source framework to build, manage, and run useful Autonomous AI Agents|
||AgentGPT|A framework allows users to configure and deploy Autonomous AI agents rapidly|

  

  

As we continue in the next few weeks, we will be  focusing in more detail on the area of  **LLM-powered AI agent**

  

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-4327370-dt-content-rid-18302_1/xid-18302_1)

  

So remember in COMP 237, we learnt the **A* algorithm,**  and created a planning agent to predict the route from the canteen to the AI Lab, and it worked pretty well in predicting the routes.

Take five minutes to think about the following question.

Should we change the agent to an LLM-powered AI agent?

If yes, state why?

If no state why?

Share your response with the professor and the class.


#### Vector Databases

  

Let us start by watching this short video to get a better idea about what Vector datastores are:

  

  

_So what is a vector database???_

**A vector database indexes and stores vector embeddings for** **fast retrieval** **and** **similarity search****, with capabilities like CRUD operations, metadata filtering, horizontal scaling, and serverless.**

Efficient data processing has become more crucial than ever for applications that involve **large language models, generative AI, and semantic search.**

All of these new applications rely on [**vector embeddings**](https://www.pinecone.io/learn/vector-embeddings-for-developers/), a type of vector data representation that carries within it semantic information that’s critical for the AI to gain understanding and maintain a long-term memory they can draw upon when executing complex tasks.

Embeddings are generated by AI models (such as Large Language Models) and have many attributes or features, making their representation challenging to manage.

_Why do we need vector databases?_

In the context of AI and machine learning, these features **represent different dimensions of the data** that are essential for **understanding patterns, relationships, and underlying structures.**

That is why we need a **specialized database designed** specifically for handling **this data type,** i.e., vector embeddings**.**

- Vector databases offer optimized storage and querying capabilities for embeddings.
- Vector databases have the capabilities of a traditional database that are absent in standalone vector indexes and the specialization of dealing with vector embeddings, which traditional scalar-based databases lack.
- The challenge of working with vector data is that traditional scalar-based databases can’t keep up with the complexity and scale of such data, making it difficult to extract insights and perform real-time analysis.
- That’s where vector databases come into play – they are intentionally designed to handle this type of data and offer the performance, scalability, and flexibility.

_How do they fit in the AI picture?_

Have a look at the diagram below:

![Vector database in AI applications](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996614-dt-content-rid-23244787_1/xid-23244787_1)

  

Image source: Pinecone

Notice: no rows or columns

Let’s break this down:

1. The [embedding model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/) is used to create vector embeddings for the content we want to index.
2. The vector embedding is inserted into the vector database, with some reference to the original content from which the embedding was created.
3. When the application issues a query, **the same embedding model** is used to create embeddings for the query and use those embeddings to query the database **for _similar_ vector embeddings**.

        Wow, that is similar to what RAG requires.

  

_How does a vector database work?_

Traditional databases store strings, numbers, and other types of scalar data in rows and columns.

A vector database **operates on vectors**, so the **way it’s optimized and queried is quite different.**

In traditional databases, we are usually querying for rows in the database where the value exactly matches our query. In vector databases, we apply a similarity metric to **find a vector that is the most similar to our query.**

A vector database uses a **combination of different algorithms** that all participate in **Approximate Nearest Neighbor (ANN)** search.

These algorithms **optimize the search** through:

- Hashing.
- Quantization.
- Graph-based search.

These algorithms are assembled into a pipeline that provides fast and accurate retrieval of the neighbors of a queried vector.

Since the vector database provides approximate results, the main trade-offs we consider are between accuracy and speed.

The more accurate the result, the slower the query will be.

However, a good system can provide ultra-fast search with near-perfect accuracy.

Have a look at the diagram below for a **common pipeline** for a vector database:

  

![Vector databasepipeline](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996614-dt-content-rid-23244786_1/xid-23244786_1)

  

Image source: Pinecone

1. **Indexing:** The vector database indexes vectors using an algorithm such as **Product Quantization PQ, Locality-Sensitive Hashing (LSH), or Hierarchical navigable small world HNSW**. This step maps the vectors to a data structure that will enable faster searching.
2. **Querying:** The vector database compares the indexed query vector to the indexed vectors in the dataset to find the nearest neighbors (applying a similarity metric used by that index)
3. **Post Processing**: In some cases, the vector database retrieves the final nearest neighbors from the dataset and post-processes them to return the final results. This step can include re-ranking the nearest neighbors using a different similarity measure.

**Important**

It is the way the **data is indexed and stored** using the algorithms such as **Product Quantization PQ, Locality-Sensitive Hashing (LSH), or Hierarchical navigable small world HNSW**  that makes the **retrieval fast.**

We will not get into these algorithms, as that is usually covered in a database course.

Some providers offer a **serverless option** to separate compute from storage.

_Who are the players?_

Have a look at the table below that shows some of the leaders in vector databases for 2025

|Feature|Chroma|Pinecone|Weaviate|Faiss|Qdrant|Milvus|PGVector|
|---|---|---|---|---|---|---|---|
|Open-source|✅|❎|✅|✅|✅|✅|✅|
|Primary Use Case|LLM Apps Development|Managed Vector Database for ML|Scalable Vector Storage and Search|High-Speed Similarity Search and Clustering|Vector Similarity Search|High-Performance AI Search|Adding Vector Search to PostgreSQL|
|Integration|LangChain, LlamaIndex|LangChain|OpenAI, Cohere, HuggingFace|Python/NumPy, GPU Execution|OpenAPI v3, Various Language Clients|TensorFlow, PyTorch, HuggingFace|Built into PostgreSQL ecosystem|
|Scalability|Scales from Python notebooks to clusters|Highly scalable|Seamless scaling to billions of objects|Capable of handling sets larger than RAM|Cloud-native with horizontal scaling|Scales to billions of vectors|Depends on PostgreSQL setup|
|Search Speed|Fast similarity searches|Low-latency search|Milliseconds for millions of objects|Fast, supports GPU|Custom HNSW algorithm for rapid search|Optimized for low-latency search|Approximate Nearest Neighbor (ANN)|
|Data Privacy|Supports multi-user with data isolation|Fully managed service|Emphasizes security and replication|Primarily for research and development|Advanced filtering on vector payloads|Secure multi-tenant architecture|Inherits PostgreSQL’s security|
|Programming Language|Python, JavaScript|Python|Python, Java, Go, others|C++, Python|Rust|C++, Python, Go|PostgreSQL extension (SQL-based)|

  

Source: Datacamp

##### In a nut-shell

The exponential growth of vector embeddings in fields such as NLP, computer vision, and other AI applications has resulted in the emergence of vector databases as the computation engine that allows us to interact effectively with vector embeddings in our applications.

Vector databases are purpose-built databases that are specialized to tackle the problems that arise when managing vector embeddings in production scenarios. For that reason, they offer significant advantages over traditional scalar-based databases and standalone vector indexes.

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996614-dt-content-rid-40901_1/xid-40901_1)

  

- Pinecone: https://www.pinecone.io/learn/vector-database/
- IBM Technology: https://www.youtube.com/watch?v=gl1r1XV0SLw
- DataCamp: https://www.datacamp.com/blog/the-top-5-vector-databases
#### **Technological challenges in LLMs**



#### Retrieval Augmented Generation (RAG)

  

##### Why Retrieval Augmented Generation?

  

Let us start by looking at how we interact with LLMs. Have a look at the figure below:

![Large language text generation task](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996613-dt-content-rid-23244782_1/xid-23244782_1)

  

Image prepared by Mayy Habayeb

This resembles any of us interacting with ChatGPT or any other language model. The problem lies in the answer.

Even the most advanced generative AI models can only **generate responses based on the data they have been trained on**.

They cannot provide **accurate** answers to questions about information **outside their training data**.

Generative AI models simply don’t know that they don’t know!

This leads to inaccurate or inappropriate outputs, sometimes called **hallucinations, bias, or, simply said, nonsense.**

  

##### What is RAG?

  

Retrieval Augmented Generation (RAG) is a **framework** that addresses this limitation by combining retrieval-based approaches with **generative models**. 

- It retrieves **relevant data** from **external sources** in **real time** and uses this data to **generate more accurate and contextually relevant responses**.
- **Generative AI** models integrated with **RAG retrievers** are revolutionizing the field with their unprecedented efficiency and power.
- One of the **key strengths** of RAG is its **adaptability.** It can be seamlessly applied to any type of data, be it **text, images, or audio.**
- This versatility makes RAG ecosystems a **reliable and efficient** tool for **enhancing generative AI capabilities**.

  

![Retrieval Augmented Generation](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996613-dt-content-rid-23244502_1/xid-23244502_1)

  

Image generated by AI

  

- When a generative AI model doesn’t know how **to answer accurately,** some say it is hallucinating or producing bias. Simply said, it just produces nonsense.
- However, it all boils down to the impossibility of providing an adequate response when the model’s training didn’t include the information requested beyond the classical model configuration issues.
- This confusion often leads to random sequences of the **most probable outputs**, not the **most accurate ones.**
- RAG begins where generative AI ends by providing the information an LLM model lacks to answer accurately.

RAG was designed (Lewis et al., 2020) for LLMs. You can download the research paper from here :

Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

  

  

This was a joint effort between Facebook AI Research, University College London, and New York University.

**The RAG framework** will perform **optimized information retrieval tasks**, and the **generation ecosystem** will add this information **to the input (user query or automated prompt) to produce improved output.** 

  

##### Type of RAG configurations

  

A RAG framework necessarily contains two main components: **a retriever** and **a generator**.

**The generator** can be any LLM or foundation multimodal AI platform or model, such as GPT-4o, Gemini, Llama, or one of the hundreds of variations of the initial architectures.

**The retriever** can be any of the emerging frameworks, methods, and tools such as Activeloop, Pinecone, LlamaIndex, LangChain, Chroma, and many more. Also you could write your own.

###### 1- Naive

  

**Naïve RAG:** This type of RAG framework doesn’t involve complex data embedding and indexing. It can be efficient to access reasonable amounts of data through keywords, for example, to augment a user’s input and obtain a satisfactory response.

Keyword search suits simple retrieval

**2- Advanced**

**Advanced RAG**: This type of RAG involves more complex scenarios, such as with vector search and index-based retrieval applied. Advanced RAG can be implemented with a wide range of methods. It can process multiple data types, as well as multimodal data, which can be structured or unstructured.

Vector search is ideal for semantic-rich documents.

Index-based search offers speed with large data.

###### A3- **Modular RAG**:

**Modular RAG:** broadens the horizon to include any scenario that involves naïve RAG, advanced RAG, machine learning, and any algorithm needed to complete a complex project.

**Example:**

A keyword search can help find clearly defined document labels, such as the titles of PDF files and labeled images, before they are processed. Then, an indexed search will group the documents into indexed subsets. Finally, the retrieval program can search the indexed dataset, find a subset, and only use vector search to go through a limited number of documents to find the most relevant one.

##### RAG versus fine-tuning

  

Sometimes you will hear the term we fine-tune a large language model, such as BERT.

_How is this different than RAG???_

- RAG is not always an alternative to fine-tuning, and fine-tuning cannot always replace RAG.
- If we accumulate too much data in RAG datasets, the system may become too cumbersome to manage.
- We cannot fine-tune a model with **dynamic**, ever-changing data such as daily weather forecasts, stock market values, corporate news, and all forms of daily events.

The decision of whether to implement RAG or fine-tune a model relies on the **proportion of parametric versus non-parametric information.**

The fundamental difference between a model trained from scratch or fine-tuned and RAG can be summed up in terms of **parametric and non-parametric** knowledge:

- **Parametric**: In a RAG-driven generative AI ecosystem, the parametric part refers to the generative AI model’s parameters (weights) learned through training data. This means the model’s knowledge is stored in these learned weights and biases. The original training data is transformed into a mathematical form, which we call a parametric representation. Essentially, the model “remembers” what it learned from the data, but the data itself is not stored explicitly.
- **Non-Parametric**: The non-parametric part of a RAG ecosystem **involves storing explicit data** that can be accessed directly. This means that the data remains available and can be queried whenever needed. Unlike parametric models, where knowledge is embedded indirectly in the weights, non-parametric data in RAG allows us to see and use the actual data for each output.

The difference between RAG and fine-tuning relies on the amount of **static (parametric)** and **dynamic (non-parametric)** ever-evolving data the generative AI model must process.

A system that relies too heavily on RAG **might become overloaded and cumbersome to manage**.

A system that relies too much on fine-tuning a generative model will display its inability to adapt to daily information updates.

**RAG and fine-tuning are not mutually exclusive.**

RAG can be used to improve a model’s overall efficiency, together with fine-tuning, which serves as a method to enhance the performance of both the retrieval and generation components within the RAG framework.

Here comes another design decision:

**Here comes another design decision:**

RAG-driven generative Designers will have to evaluate the potential of the ecosystem’s **trained parametric generative AI** model before implementing a non-parametric (explicit data) RAG framework.

The potential of the RAG component requires careful evaluation as well.

In the end, the balance between enhancing the retriever and the generator in a RAG-driven generative AI ecosystem **depends on a project’s specific requirements and goals.**

  

![The decision-making threshold between enhancing RAG or fine-tuning an LLM](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996613-dt-content-rid-23244783_1/xid-23244783_1)

  

_The decision-making threshold between enhancing RAG or fine-tuning an LLM_

Image source:  RAG-Driven Generative AI by Denis Rothman published by Packt Publishing  

#### The RAG Ecosystem

  

**Have a look at the diagram below that illustrates the ecosystem for RAG:**

  

![Retrieval Augmented Generation Eco system](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996613-dt-content-rid-23244784_1/xid-23244784_1)

  

  

Image source:  RAG-Driven Generative AI by Denis Rothman published by Packt Publishing  

1. The Retriever (D) handles data collection, processing, storage, and retrieval
2. The Generator (G) handles input augmentation, prompt engineering, and generation
3. The Evaluator (E) handles mathematical metrics, human evaluation, and feedback
4. The Trainer (T) handles the initial pre-trained model and fine-tunes the model

Each of these four components relies on its respective ecosystems, which form the overall R**AG-driven generative AI pipeline**. 

##### The retriever (D)

The retriever component of a RAG ecosystem collects, processes, stores, and retrieves data. The starting point of a RAG ecosystem is thus an ingestion data process, of which the first step is to collect data.

###### Collect (D1)

In today’s world, AI data is as diverse as our media playlists. It can be anything from:

- A chunk of text in a blog post t
- A memo
- The latest hit song streamed through headphones (MP3, MP4)
- Emails
- Images (PNG, JPG)
- PDF documents
- Web pages
- ....

These files themselves come in all shapes and sizes.

A large proportion of this data is unstructured and found in unpredictable and complex ways.

Many platforms, such as **Pinecone, OpenAI, Chroma, and Activeloop**, provide ready-to-use tools to process and store this data.

###### Process (D2)

- These data objects are then transformed to create **uniform feature representations.**
- Data can be **chunked** (broken into smaller parts), **embedded (transformed into vectors)**, and **indexed to enhance searchability** and retrieval efficiency.

###### Storage (D3)

- Vector stores like Deep Lake, Pinecone, and Chroma come into play.
- These are super smart libraries that don’t just store your data but convert it into mathematical entities as vectors, enabling powerful computations.
- They can also apply a variety of indexing methods and other techniques for rapid access.

It is a design decision at the end of the day

###### Retrieval query (D4)

- The retrieval process is triggered by the user input or automated input (G1).
- To retrieve data quickly, we load it into vector stores and datasets after transforming it into a suitable format.
- Then, using a combination of keyword searches, smart embeddings, and indexing, we can retrieve the data efficiently.
- Cosine similarity, for example, finds items that are closely related, ensuring that the search results are not just fast but also highly relevant.
- Once the data is retrieved, we then augment the input.

##### **The generator (G)**

The lines are blurred in the RAG ecosystem between input and retrieval, as shown in _Figure 1.3_, representing the RAG framework and ecosystem. The user input (G1), automated or human, interacts with the retrieval query (D4) to augment the input before sending it to the generative model.

The generative flow begins with an input.

###### Input (G1)

The input can be:

1. A batch of automated tasks (processing emails, for example)
2. human prompts through a **User Interface** (**UI**).

This flexibility allows you to seamlessly integrate AI into various professional environments, enhancing productivity across industries.

###### Augmented input with HF (G2)

- Human feedback (HF) can be added to the input.  
- Human feedback will make a RAG ecosystem considerably adaptable and provide full control over data retrieval and generative AI inputs.

###### Prompt engineering (G3)

- Both the retriever (D) and the generator (G) rely heavily on prompt engineering to prepare the standard and augmented message that the generative AI model will have to process.
- Prompt engineering brings the retriever’s output and the user's input together.

###### Generation and output (G4)

- The choice of a generative AI model depends on the goals of a project. Llama, Gemini, GPT, and other models can fit various requirements.
- The prompt must meet each model’s specifications.
- Frameworks such as LangChain help streamline the integration of various AI models into applications by providing adaptable interfaces and tools.

###### **The evaluator (E)**

We often rely on mathematical metrics to assess the performance of a generative AI model. However, these metrics only give us part of the picture. It’s important to remember that the ultimate test of an AI’s effectiveness comes down to human evaluation.

###### Metrics (E1)

- A model cannot be evaluated without mathematical metrics, such as cosine similarity, as with any AI system.
- These metrics ensure that the retrieved data is relevant and accurate.
- By quantifying the relationships and relevance of data points, they provide a solid foundation for assessing the model’s performance and reliability.

###### Human feedback (E2)

- No generative AI system, whether RAG-driven or not, and whether the mathematical metrics seem sufficient or not, can elude human evaluation.
- It is ultimately human evaluation that decides if a system designed for human users will be accepted or rejected, praised or criticized.

##### **The trainer (T)**

- A standard generative AI model is pre-trained with a vast amount of general-purpose data.
- Then, we can fine-tune (T2) the model with domain-specific data.

  

Have a look at the diagram below that shows one possible implementation for the second type, Advanced RAG:

![Retrieval Augmented Generation example](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996613-dt-content-rid-23244785_1/xid-23244785_1)

  

  

Image prepared by Mayy Habayeb

---

#### **Why is it important from your end as an AI software designer?**

  

Here you would need to put on your **design hat** and make some design decisions:

For example:

1. Where and how are you going to store the data?
2. How are you going to retrieve the data?
3. Which LLMs would you use to embed the data? If there aren’t any, are you going to train your own embeddings?
4. Which  LLM will you use to generate the data?
5. Is there any cost?
6. Would you need to fine-tune the LLM?
7. How will you involve humans in the loop?
8. .....................................

Explain the design decisions

  

I

#### Embeddings

  

You will be hearing this word quite a lot as you move forward in your AI career.

  

_So, what are embeddings?_

**Embeddings are a learnable** **data representation** **that maps high-cardinality data into a lower-dimensional space in such a way that the information relevant to the learning problem is preserved.**

**Embeddings** **are at the heart of modern-day machine learning and have various incarnations throughout the field****.**

###### Embeddings

  

They are basically a representation of different types of data **text, images, and videos,** into **densed vectors of numbers.**

Have a look at the image on the right.

**Embeddings**

![Embedding models](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996612-dt-content-rid-23244780_1/xid-23244780_1)

  

Image source: OpenCV  https://opencv.org/blog/vector-embeddings/ 

_So what is the problem, and why do we need such a representation??_

##### **Problem**

  

Machine learning models systematically look for patterns in data that capture how the properties of the model’s input features relate to the output label.

As a result, the data representation of the input features directly affects the quality of the final model.

While handling structured, numeric input is fairly straightforward, the data needed to train a machine learning model can come in myriad varieties, such as **categorical features, text, images, audio, time series, and many more**.

For these data representations, we need a **meaningful numeric value** to supply our machine learning model so these features can fit within the typical training paradigm.

##### Solution

The Embeddings design pattern addresses the problem of representing high-cardinality data densely in a lower dimension by passing the input data through an **embedding layer** that has **trainable weights**. 

The **weights** in the embedding layer would be learned as part of the gradient descent procedure when training the model.

_Don’t worry now about how the training is done; we will cover the details of this training in the deep learning and NLP courses._

Embeddings provide a way to handle some of these disparate data types in a way that **preserves similarity** between items and thus improves our model’s ability to learn those essential patterns.

##### **Example:**

Assume we are trying to predict a **baby’s weight** based on four features:

1. **is_male:** Categorical can take three values: true, false, unknown
2. **mother_age:** Numeric range
3. **gestation_weeks:** Numeric range
4. **plurality:** Categorical can take one of six values: Single(1), Twins(2), Triplets(3), Multiple(2+), Quadruplets(4), Quintuplets(5)

Download the CSV file and examine the data

babyweight_sample.csv

  

Let us focus on the data representation of the last feature, **plurality,** and try to represent it in two different ways:

1. One-hot-encoding
2. Embeddings

##### One-hot-encoding

 We can represent using one-hot encoding, so each of the six values would be represented by a vector, the size of the **vector is six**,  as per the table below:

|   |   |
|---|---|
|Plurality|One-hot encoding|
|Single(1)|[1,0,0,0,0,0]|
|Multiple(2+)|[0,1,0,0,0,0]|
|Twins(2)|[0,0,1,0,0,0]|
|Triplets(3)|[0,0,0,1,0,0]|
|Quadruplets(4)|[0,0,0,0,1,0]|
|Quintuplets(5)|[0,0,0,0,0,1]|

##### Embeddings

Now, let us assume we use an embedding representation instead. Remember, embeddings are **dense vectors** i.e., the size is usually smaller, and something we controlduring the training process:

|   |   |
|---|---|
|Plurality|Learned encoding|
|Single(1)|[0.4, 0.6]|
|Multiple(2+)|[0.1, 0.5]|
|Twins(2)|[-0.1, 0.3]|
|Triplets(3)|[-0.2, 0.5]|
|Quadruplets(4)|[-0.4, 0.3]|
|Quintuplets(5)|[-0.6, 0.5]|

##### **_The burning question: How do we get embeddings??_**

  

To get an embedding data representation, we need an **embedding Model****.** We have to either:

1- Train our own embedding model (Need a lot of data and computational resources) **☹ ☹ ☹**

**Or**

2- Use an embedding pre-trained model   **😊**

_And guess what ??_

Some Large **language models (LLMs)**  have been trained just to generate embeddings.

In our lab exercise, we will use one of the LLMs to generate embeddings. **😊😊😊**

  

![Flame image](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996612-dt-content-rid-9141564_1/xid-9141564_1)

  

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996612-dt-content-rid-18302_1/xid-18302_1)

  

Take ten minutes to search for ready-to-use embedding models:

- Check Meta, OpenAI, Google, DeepSeek...etc.
- Check if any are open source
- Check the options for the embedding dimensions
- Check if there are any costs.

Share with the class, click the class conversation and type in your response.

_What are the advantages of using embeddings:_

1- Well, first, the size of the data that needs to be loaded in the memory would be much less than the data represented as normal vectorized representations, like one-hot encoding and bag of words.

2- Second, embeddings **capture closeness relationships** in the input data in a lower-dimensional representation. We can use an embedding layer as a replacement for clustering techniques (e.g., customer segmentation) and dimensionality reduction methods like principal components analysis (PCA).

Embedding weights are determined in the main model training loop, thus saving the need to cluster or do PCA beforehand.

##### Closeness of relationships

  

During building embeddings, the models learn weights. A learned embedding allows us to extract **inherent similaritie**s between two separate categories, and given that there is a numeric vector representation, we can precisely quantify the similarity between two categorical features.

Let us get back to our example

##### One-hot-encoding similarity

Have a look at the similarity matrix below:

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
||Single(1)|Multiple(2+)|Twins(2)|Triplets(3)|Quadruplets(4)|Quintuplets(5)|
|Single(1)|1|0|0|0|0|0|
|Multiple(2+)|-|1|0|0|0|0|
|Twins(2)|-|-|1|0|0|0|
|Triplets(3)|-|-|-|1|0|0|
|Quadruplets(4)|-|-|-|-|1|0|
|Quintuplets(5)|-|-|-|-|-|1|

  

By only using one-hot encoding, any values will only be similar to itself.

##### Embeddings

  

![Embeddings similarity](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996612-dt-content-rid-23244781_1/xid-23244781_1)

  

  

If we plot the vectors in a 2D space, we will see that some vectors are closer to each other than others. The occurrence of quadruplets and quintuplets likely affects the birthweight in a statistically similar way as opposed to single child birthweights.

##### Text embeddings

  

Text provides a natural setting where it is advantageous to use an embedding layer. Given the cardinality of a vocabulary (often on the order of tens of thousands of words), one-hot encoding each word isn’t practical.

This would create an incredibly large (high-dimensional) and **sparse matrix** for training.

Also, **we’d like similar words to have embeddings close by** and unrelated words **to be far away** in embedding space. Therefore, we use a dense word embedding to vectorize the discrete text input before passing to our model.

##### Image embeddings

  

While text deals with very sparse input, other data types, such as images or audio, consist of dense, high-dimensional vectors, usually with multiple channels containing raw pixel or frequency information.

In this setting, an Embedding captures a **relevant, low-dimensional representation of the input.**

---

#### **Why is it important from your end as an AI software designer?**

  

Well, all of this needs to be taken into consideration as software components in your design. You might need a component to train embeddings, or a component to load a pre-trained model, or a component to check your corpus against the pretrained vectors.

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996612-dt-content-rid-40901_1/xid-40901_1)

  

- Chapter 2 "Machine Learning Design Patterns" by Valliappa Lakshmanan, Sara Robinson, and Michael Munn published by O'Reilly.







  
**Introduction To Hugging Face**

Hugging Face hosts a vast collection of resources with **over 500,000 models**, **more than 100,000 datasets**, and **thousands of Spaces** for interactive AI demos. These tools span a wide range of domains including natural language processing, computer vision, speech, and reinforcement learning.

The platform is supported by a large and active community of **researchers, developers, educators, and enthusiasts** who contribute models, datasets, and applications regularly. This vibrant ecosystem makes Hugging Face a go-to resource for collaborative AI development.

Many leading companies and organizations use Hugging Face tools in their workflows, including **Google**, **Microsoft**, **Amazon**, **Meta**, **NVIDIA**, **Intel**, **ServiceNow**, and **Bloomberg**, as well as numerous startups, universities, and research labs around the world.

**What is Hugging Face?**

- Hugging Face is a platform and community that brings together AI enthusiasts, researchers, and developers. It is designed to make artificial intelligence more accessible, encourage open sharing of resources, and promote collaboration across the AI ecosystem.

  

![Hugging Face is similar to GitHub](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996577-dt-content-rid-23244751_1/xid-23244751_1)

  

On Hugging Face, users can explore the latest advancements in artificial intelligence and access a variety of tools to build, fine-tune, and experiment with AI models. The platform features a growing collection of cutting-edge models across different domains and encourages collaboration by connecting users with a global community of AI enthusiasts and practitioners.

  

Hugging Face offers a range of tools to support AI development, including:

  

- **Hugging Face Hub**: A central repository to share, discover, and manage models, datasets, and spaces.
- **Transformers**: A popular library for natural language processing (NLP) tasks using pre-trained models.
- **Datasets**: A library for easily accessing and sharing datasets for machine learning projects.
- **Tokenizers**: A fast and flexible library for text tokenization.
- **AutoTrain**: A no-code tool to train and deploy machine learning models.
- **Inference API**: A hosted service to run models in the cloud without managing infrastructure.
- **Spaces**: A platform to build and share interactive ML demos using Gradio or Streamlit.

These tools help streamline the process of building, testing, and deploying AI models.

  

**Hugging Face Hub**

The Hugging Face Hub is a central platform where users can share, discover, and manage machine learning models, datasets, and applications. It hosts over **500,000 models**, **100,000 datasets**, and **thousands of interactive Spaces**, making it one of the largest repositories for open AI resources. The Hub supports collaboration, versioning, and community contributions.

  

![picture of hub datasets](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996577-dt-content-rid-23244750_1/xid-23244750_1)

  

Take a look at some of the well-known LLMs that are available on the Hub.

![llms picture](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996577-dt-content-rid-23244755_1/xid-23244755_1)

  

  

  

**Transformers**

The most valuable offering from Hugging Face is the **Transformers** Python library. This library allows users to access thousands of pre-trained models through a simple API and facilitates the creation of machine learning pipelines for various tasks. It provides state-of-the-art natural language processing models and supports both **PyTorch** and **TensorFlow** frameworks. Key features include easy model fine-tuning, comprehensive documentation with examples, regular updates, and strong community support. The Transformers library is widely adopted for tasks such as text classification, translation, question answering, and more, making it an essential tool for modern AI development.

**Datasets**

The Datasets library provides access to a large and diverse collection of datasets used for training and evaluating machine learning models. It simplifies loading, preprocessing, and sharing data, supporting seamless integration with other Hugging Face tools.

**Tokenizers**

Tokenizers is a fast and customizable library for text preprocessing. It supports efficient tokenization across multiple languages and is designed to handle large-scale datasets, making it ideal for modern NLP pipelines.

**AutoTrain**

AutoTrain is a no-code solution that automates the entire process of training, tuning, and deploying machine learning models. With just a few clicks, users can turn raw data into a functional model, making AI development more accessible to everyone.

**Inference API**

The Inference API allows developers to run models directly from the Hugging Face Hub in the cloud. It eliminates the need for managing infrastructure and enables quick deployment of models into real-world applications via simple API calls.

**Spaces**

Spaces is a platform for building and hosting interactive machine learning applications with easy to use GUI using Gradio or Streamlit. Users can showcase their models through live demos, encouraging collaboration, feedback, and experimentation.

Take a look at some of the ML Demos and/or Apps hosted on Spaces.

  

![Huggging Face spaces](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996577-dt-content-rid-23244765_1/xid-23244765_1)

  

**Summary**

Hugging Face has transformed the way the AI community builds, shares, and collaborates on machine learning projects. With its extensive collection of models, datasets, and powerful tools like Transformers and AutoTrain, it lowers barriers to entry and accelerates innovation. Supported by a vibrant global community and trusted by leading companies worldwide, Hugging Face continues to drive open, accessible, and cutting-edge advancements in artificial intelligence.
##### **1- Hallucination**

  

Bang et al. (2023) found that, similarly to other LLMs, ChatGPT suffers from **hallucination** problems that refer to the phenomenon of LLMs generating plausible‐sounding but incorrect or unsupported information in their responses. This issue can be particularly problematic because it can lead to the dissemination of false or misleading information. However, the interactive feature of ChatGPT enables human collaboration with the underlying LLM to improve its performance through a multi‐turn ‘prompt engineering’ fashion, i.e., an interactive approach in which users iteratively engage with a large language model (LLM) like ChatGPT in a conversational manner.

Have a look at the image below, do you notice anything odd:

  

![Hallucination](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996611-dt-content-rid-23244742_1/xid-23244742_1)

  

  

  

  

###### **Image source:** **Ref: oronto.ctvnews.ca/three-armed-person-mistakenly-exposes-ai-generated-images-in-toronto-mayoral-platform-1.6439117**

  

###### CTV News Toronto:

A Toronto mayoral candidate’s use of AI-generated images was exposed when a photograph of a person with three arms appeared in their campaign platform.

  

##### **2- Tools tend to form themselves to the conversation, affirmative in nature.**

  

LLMs tune themselves into the user’s conversation, making the user believe that they are on the user’s side, supporting the user’s line of thinking, creating an affirmation bias.

Have a look at the example below from euronews.next:

![Euro news logo](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996611-dt-content-rid-23244737_1/xid-23244737_1)

  

  

  

  

A man ends his life after an AI chatbot 'encouraged' him to sacrifice himself to stop climate change.

A Belgian man reportedly decided to end his life after having conversations about the future of the planet with an AI chatbot named Eliza.

"A Belgian man reportedly ended his life following a six-week-long conversation about the climate crisis with an artificial intelligence (AI) chatbot. According to his widow, who chose to remain anonymous, *Pierre - not the man’s real name - became extremely eco-anxious when he found refuge in Eliza, an AI chatbot on an app called Chai. Eliza consequently encouraged him to put an end to his life after he proposed sacrificing himself to save the planet."

                                                                                                                                             [Euronew.next By Imane EL Atillah Published on 31/03/2023 - 17:37•Updated 19:28]

  

##### **3- Copyright violation**

It’s still not clear how language models and their outputs fit into copyright law.

Have a look at the examples below:

1- A lawsuit claims that Copilot violated the Free Software Foundation’s General Public License (GPL) by generating code using a model that was trained on GPL-licensed code.

  

  

![Copyright violation copilot](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996611-dt-content-rid-23244735_1/xid-23244735_1)

  

2- AI-created images lose U.S. copyrights in test for new technology

The below was the news on **Reuters**:

February 22, 2023 8:41 PM ESTUpdated February 22, 2023

By [Blake Brittain](https://www.reuters.com/authors/blake-brittain/)

Feb 22 (Reuters) - Images in a graphic novel that were created using the artificial-intelligence system Midjourney should not have been granted copyright protection, the U.S. Copyright Office said in a letter seen by Reuters.

"Zarya of the Dawn" author Kris Kashtanova is entitled to a copyright for the parts of the book Kashtanova wrote and arranged, but not for the images produced by Midjourney, the office said in its letter, dated Tuesday.

The decision is one of the first by a U.S. court or agency on the scope of copyright protection for works created with AI, and comes amid the meteoric rise of generative AI software like Midjourney, Dall-E and ChatGPT.

The Copyright Office said in its letter that it would reissue its registration for "Zarya of the Dawn" to omit images that "are not the product of human authorship" and therefore cannot be copyrighted.

The Copyright Office had no comment on the decision.

Kashtanova on Wednesday called it "great news" that the office allowed copyright protection for the novel's story and the way the images were arranged, which Kashtanova said "covers a lot of uses for the people in the AI art community."

The legal complexity attached to the very originality of the creation and correct ownership can be most perplexing.

##### **4- Prompt injection in LLM**

  

Prompt injection attacks exploit vulnerabilities in language models by manipulating prompts to elicit unintended behavior or access sensitive information. Attackers employ various techniques, including crafting prompts, bypassing filters, exploiting weaknesses in tokenization or encoding, and misleading the model with contextual manipulation. Understanding these attack vectors is crucial for developing effective security measures and ensuring the integrity of AI systems.

![prompt injection in LLMs](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996611-dt-content-rid-23244758_1/xid-23244758_1)

  

##### **5- Quality of data and bias**

  

The generative models are largely aided by the **quality and diversity** of data in the **training dataset**.

Any model trained with **biased or unrepresentative** data will reproduce outputs with the **same kind of bias,** hence solidifying existing biases or allowing marginalization of one or several groups in case of bias in the training data.

As with any machine learning problem, analysis of the data and knowing the **data distribution across features** is often helpful. Data analysis can reveal imbalances that can introduce bias in the model. 

As they depend on the data in the training dataset, their knowledge is a fixed knowledge base, which results in a **knowledge cutoff or** **temporal limitation** problem where they are unaware of recent events.

##### 6- Data privacy

  

Multiple experiments and researchers have proven that LLMs have a **propensity to leak data they are trained on.**

This is especially problematic if the models are trained on large amounts of private or **proprietary information**.

Special techniques and styles of prompting LLMs have shown that it is sufficient to coerce the model to generate data that includes verbatim text from its training dataset.

These prompting techniques **are not sophisticated and often make it a very easy, cost-effective attack vector to get a model to leak information.**

**Example:**

In the paper named **"Scalable Extraction of Training Data from (Production) Language Models"**

Researchers were able to spend only $200 worth of API calls to OpenAI’s GPT-3.5 model and use prompt injection techniques to coerce the model to leak private information.

The leaked information includes people’s names, email addresses, physical addresses, and phone numbers that were inadvertently present in the model’s training dataset.

##### 7- Computational resources

  

Training sophisticated generative models is very **resource-intensive** and requires **high computational power**; this often makes it economically cost-prohibitive and energy-consuming to train large language models. 

Training large models such as GPT-3 is estimated to cost millions of dollars in compute resources alone. T

The exact cost depends on factors such as:

- Model size
- Training duration
- Hardware efficiency.

For example, training GPT-3 was estimated to cost around $4–5 million in compute resources, and more recent models such as GPT-4 and PaLM are likely even more expensive to train. 

Beyond the hardware itself, there are significant infrastructure costs related to:

- Power consumption.
- Cooling
- Data center space

Due to the high costs, training large language models is primarily done by large tech companies or well-funded research institutions.

Cloud services now offer access to pre-trained models and fine-tuning capabilities, making some level of LLM work more accessible to smaller organizations and the general public.

A way to overcome this challenge can be found in recent innovations with small language models (SLMs).

These are much smaller generative AI models that can be trained to achieve specific tasks.

Even though these models are limited to a very narrow set of domain-specific tasks, it is much more economical to train these models since they require far fewer computational resources.

##### 8- Generalization and creativity

  

- One of the big problems with these generative AI models is that **their generalization ability** turns out to be very poor.
- They seldom generate content that is strikingly different from the training data.
- That is, they are brilliant at copying the repeating patterns but fail really to create something original or novel.
- As a consequence, their potential for capital C creativity stays very limited.

With the new wave of models introduced in 2025, more has been done to address this challenge. OpenAI, with its new GPT5 model, claims that they have much better abilities to generate and create software.

##### 9- Deepfakes and misinformation

  

GenAI is able to produce **very realistic, synthetically generated content**.

If that were to happen, it would yield **deepfakes or even misinformation,** which could be a threat to privacy, security, or even public trust.
#### **Large Language Models (LLMs)**

  

Let us start by watching this short video to get a better idea about what Large language models are:

  

_So what is a Large Language Model????_

###### Large Language Model

A **large language model** (**LLM**) is a large-scale language model notable for its ability to achieve general-purpose language understanding and generation.

LLMs acquire these abilities by using massive amounts of data to learn billions of parameters during training and consuming large computational resources during their training and operation. LLMs are artificial neural networks (mainly transformers) and are (pre)trained using self-supervised learning and semi-supervised learning.

**History**

In 2017, researchers at Google published a paper that proposed a novel neural network architecture for sequence modeling. Dubbed the Transformer, this architecture outperformed recurrent neural networks (RNNs) on machine translation tasks, both in terms of translation quality and training cost.

In parallel, an effective transfer learning method called ULMFiT showed that training long short-term memory (LSTM) networks on a very large and diverse corpus could produce state-of-the-art text classifiers with little labeled data.2

These advances were the catalysts for two of today’s most well-known transformers: the Generative Pretrained Transformer (GPT) and Bidirectional Encoder Representations from Transformers (BERT).

 By combining the Transformer architecture with unsupervised learning, these models removed the need to train task-specific architectures from scratch and broke almost every benchmark in NLP by a significant margin.

###### Today

  

 Since the release of GPT and BERT, a zoo of transformer models has emerged; a timeline of the most prominent entries is shown in

The following figure:

![LLM history since transformer](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996607-dt-content-rid-23244752_1/xid-23244752_1)

  

Image source: Zhao et al," A Survey of Large Language Models"

The below figure illustrates the evolution process of the four generations of language models (LM) from the perspective of **task-solving** capacity.

  

  

![History of NLP](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996607-dt-content-rid-23244748_1/xid-23244748_1)

  

  

Image source: Zhao et al," A Survey of Large Language Models"

As seen from above, the research of LLM has received extensive attention in the literature, which can be divided into four major development stages:

##### **1- Statistical language models (SLM)**

  

- **Models** are developed based on **statistical learning methods** that rose in the 1990s.
- The basic idea is to build the word prediction model based on the Markov assumption, e.g., predicting the next word based on the most recent context.
- The SLMs with a fixed context **length n** are also called **n-gram language models**, e.g., **bigram and trigram** language models.
- SLMs have been widely applied to enhance task performance in **information retrieval (IR)** and **natural language processing (NLP**).
- However, they often suffer from the **curse of dimensionality**: it is difficult to accurately estimate high-order language models since an exponential number of transition probabilities need to be estimated.

##### **2- Neural language models (NLM)**

  

- NLMs characterize **the probability of word sequences** by **neural networks**, e.g., multi-layer perceptron (MLP) and recurrent neural networks (RNNs). 
- The work in this stage introduced the concept of **distributed representation** of words and built the word prediction function conditioned on the aggregated context features (i.e., the distributed word vectors).
- A general neural network approach was developed to build a unified, end-to-end solution for various NLP tasks by extending the idea of learning effective features for text data.
- Word2vec was proposed to build a simplified shallow neural network for learning distributed word representations, which were demonstrated to be very effective across a variety of NLP tasks.
- These studies have initiated the use of language models for representation learning (beyond word sequence modeling), impacting the field of NLP.

##### **3- Pre-trained language models (PLM)**

  

- As an early attempt, ELMo was proposed to capture context-aware word representations by first pre-training a **bidirectional LSTM (biLSTM)** network (instead of learning **fixed word** representations) and then **fine-tuning** the biLSTM network according to specific downstream tasks.
- Based on the highly parallelizable Transformer architecture with self-attention mechanisms, BERT was proposed by **pre-training bidirectional language models** with specially designed pre-training tasks on large-scale unlabeled corpora.
-  These **pre-trained context-aware word representations** are very effective as general-purpose semantic features, which have largely raised the performance bar of NLP tasks.
- This study has inspired a large number of follow-up works, which set the **“pre-training and fine-tuning”** learning paradigm.
- Following this paradigm, a great number of studies on PLMs have been developed, introducing either different architectures (e.g., GPT-2 and BART ) or improved pre-training strategies.
- This paradigm often requires fine-tuning the PLM to adapt to different downstream tasks.

##### **4- Large language models (LLM)**

  

- Researchers find that **scaling PLM** (e.g., scaling model size or data size) often leads to an improved model capacity on downstream tasks (i.e., following the scaling law). A number of studies have explored the performance limit by training an ever larger PLM (e.g., the 175B-parameter GPT-3 and the 540B-parameter PaLM).
- Although scaling is mainly conducted in model size (with similar architectures and pre-training tasks), these large-sized PLMs display different behaviors from smaller PLMs (e.g., 330M-parameter BERT and 1.5 B-parameter GPT-2) and show surprising abilities (called **emergent abilities**) in solving a series of complex tasks.
- **For example**, GPT-3 can solve few-shot tasks through in-context learning, whereas GPT-2 cannot do well.
- Thus, the research community coined the term **“large language models (LLM)”** for these large-sized PLMs.
-  A remarkable application of LLMs is **ChatGPT2**, which adapts the LLMs from the GPT series for dialogue and presents an amazing ability to have conversations with humans. 
- **The language model is not a new technical concept,** especially for LLMs, but has evolved with the advances of artificial intelligence over the decades.
- Early language models mainly aim to model and generate text data, while the latest language models (e.g., GPT-4) focus on **complex task-solving**. 

#### The Landscape of LLMs

  

Look at the figure below, which is noted in the recent survey paper, which you can download from [A survey for large language models](https://arxiv.org/pdf/2303.18223). The authors show a timeline of existing large language models (having a size larger than 10B) in recent years. The timeline was established mainly according to the release date (e.g., the submission date to arXiv) of the technical paper for a model. If there was no corresponding paper, the authors set the date of a model as the earliest time of its public release or announcement.

They have marked the LLMs with publicly available model checkpoints in yellow. Due to the space limit of the figure, they only include the LLMs with publicly reported evaluation results.

![Figure showing LLM landscape](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996607-dt-content-rid-23244753_1/xid-23244753_1)

  

Notice the rate of introducing language models, we’re talking months.

  

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996607-dt-content-rid-18307_1/xid-18307_1)

  

To check the latest models up to August 2025, chec this website:

   [23 Best Large Language Models (LLMs) in 2025](https://backlinko.com/list-of-llms)
#### Gentrative AI

  

Let us start by watching this short video to get a better idea about what Generative AI.

  

_So what is Generative AI????_

###### Generative AI

Generative AI research is pushing creative expression forward by giving people tools to quickly and easily create new content.”   **[Meta]**

Generative AI refers to deep-learning models that can generate high-quality text, images, and other content based on the data they were trained on ”   **[IBM]**

  

**Generative AI** refers to a class of AI technologies that is capable of generating various forms of content, including but not limited to text, images, audio, and video. These AI systems can generate new content, based on their training data and input parameters, which usually include text prompts but can also involve other forms of input such as images.

The recent buzz around generative AI comes from the simplicity with which new user interfaces powered by this AI technology can create high-quality text, graphics, and videos in seconds

For the most part, generative AI uses sophisticated systems – like GPT-3, GPT-4, Jurassic, and Bloom – to create new content, which can be in the form of text, audio, images, and even video. In some cases, the result can be quite creative and compelling.

Let us look at some examples:

###### Deep Fake

  

![Image generated by deep fake](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996602-dt-content-rid-23244736_1/xid-23244736_1)

  

A deep fake image

 Image source: Generative AI with Python and TensorFlow 2 by Joseph Babcock and Raghav Bali

###### Fake news

![fake news](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996602-dt-content-rid-23244739_1/xid-23244739_1)

  

A chatbot dialogue created using GPT-2 

Ref: Generative AI with Python and TensorFlow 2 by Joseph Babcock and Raghav Bali

###### Important

Generative AI is potentially a disruptive technology. 

_So how is generative AI different from traditional AI???_

##### **​Traditional AI**

Traditional AI algorithms may be used to identify patterns within a training data set and make predictions.

                                                                                                           **[Investopedia]**       

  

##### **Discriminative AI**

The purpose is to create a mapping between a set of input variables and a target output. The target output could be a set of discrete classes (such as which word in the English language appears next in a translation), or a continuous outcome (such as the expected amount of money a customer will spend in an online store over the next 12 months)

**The output is usually a prediction or a discovered pattern.**

![traditional AI output](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996602-dt-content-rid-23244766_1/xid-23244766_1)

  

###### ​Generative AI

Generative AI is a type of artificial intelligence that can produce content such as audio, text, code, video, images, and other data. Generative AI can produce outputs in the same medium in which it is prompted (e.g., text-to-text) or in a different medium from the given prompt (e.g., text-to-image or image-to-video) 

                                                                                                                **[Investopedia]**

##### **Generative AI**

Generative AI models don't compute a score or label from input variables, but rather generate new data. Unlike discriminative models, the input variables are often vectors of numbers that aren't related to real-world values at all, and are often even randomly generated.

**The output is new content, which could be text, images, or videos:**

![Gen AI output](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996602-dt-content-rid-23244741_1/xid-23244741_1)

  

  

In very simple terms, generative AI is about making **new data** that **looks like** the data from which it **has been trained**.

In other words, learning **the underlying patterns, structures, and distributions** of input data enables a procedure within the model, allowing it to generate new data in a similar way.

**Example:**

If trained on a dataset of human faces, a generative AI model will be able to create completely new faces of people that don’t actually exist in real life but are very realistic.

_But how does Gen AI do it?_

In essence, generative AI models work by learning the **probability distribution** of a dataset and then **sampling from that distribution** to create new instances.

Don't worry just now about the details of how this works they will be covered in future courses.

#### Use Cases for generative AI

  

The use cases for generative AI models are endless. 

Have a look at the figure below, which illustrates some of the areas where Generative AI is being used:

  

![Use cases of Gen AI](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996602-dt-content-rid-23244768_1/xid-23244768_1)

###### Auto code generation:  

Generative AI for coding is possible because of recent breakthroughs in large language model (LLM) technologies and natural language processing (NLP). It uses deep learning algorithms trained on vast datasets of diverse existing source code. Training code generally comes from publicly available code produced by open-source projects.

Have a look at the figure below:

![Gen AI for coders](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996602-dt-content-rid-23244740_1/xid-23244740_1)

Below is a list of products in the market:

- Copilot X
- AlphaCode
- Tabnine
- Magic
- PolyCoder
- Blaze

###### Legal:

Do not pay is one of the first to enter the AI code generation category in 2017. The system uses generative AI to help automate the process for canceling subscriptions, receiving refunds, and filing claims.

The most interesting application of generative AI came in 2023. DoNotPay was prepared to use its technology as the “lawyer” for a traffic court case. The AI could hear and understand the people in the courtroom. It could advise the defendant on what to say (they would do this by wearing headphones). The legal community was not impressed and pushed back hard 😞

###### Customer service and sales, and marketing:

For example

Anyword uses an LLM to generate text and understand the language to generate:

- messaging briefs
- suggests article topics
- builds outlines
- research summaries
- improves existing copy

Cresta: helps sales and service organizations to communicate with prospects and customers

INK: A platform to help develop better content that gets high rankings. Uses sophisticated generative adversarial networks for the visual content and transformer-based models for the text content. There is also the use of reinforcement learning to shape the content for search intent.

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996602-dt-content-rid-40901_1/xid-40901_1)

  

- Chapter 1: “Building Agentic AI Systems”, 2025, by Anjanava Biswas and Wrick Talukdar, published by Packtpub.
- Generative AI How ChatGPT and Other AI Tools Will Revolutionize Business, by Tom Taulli, 2023, published by Apress
- Images: Generative AI with Python and TensorFlow 2 by Joseph Babcock and Raghav Bali
- Investopedia
#### Design pattern "Continued Model Evaluation"

  

##### **Motivation:**

  

Problem of needing to take action when a deployed model **is no longer fit-for-purpose**.

**_But wait, how can a model not be fit for the purpose????_**

So, you’ve trained your model. You collected the raw data, cleaned it up, engineered features, created embedding layers, tuned hyperparameters, the whole shebang. You’re able to achieve 96% accuracy on your hold-out test set.

**Amazing!** You’ve even gone through the painstaking process of deploying your model, taking it from a Jupyter notebook to a machine learning model in production, and are serving predictions via a REST API. Congratulations, you’ve done it.

**Are you finished????**

Well, not quite.

- Deployment is not the end of a machine learning model’s life cycle.
- How do you know that your model is working as expected in the wild?
- What if there are unexpected changes in the incoming data?
- Or the model no longer produces accurate or useful predictions? How will these changes be detected?

The world is **dynamic**, but developing a machine learning model usually creates a **static model** from historical data.

This means that once the model goes into production, it can start to **degrade** and its **predictions can grow increasingly unreliable**.

**Why do models degrade over time???**

**Two reasons:**

**_1- Concept drift_**

**_2-  Data drift_**

Let us have a closer look at each:

##### **Concept drift**

  

**Concept drift** occurs whenever the relationship between the model inputs and target has changed.

This often happens because the underlying assumptions of your model have changed, such as models trained to learn adversarial or competitive behavior, like:

- fraud detection
- spam filters
- stock market trading
- online ad bidding,
- cybersecurity.

In these scenarios, a predictive model aims to **identify patterns** that are characteristic of desired (or undesired) activity, while the adversary learns to adapt and may modify their behavior as circumstances change.

**Example:**

A model developed to detect credit card fraud. The way people use credit cards has changed over time, and thus, the common characteristics of credit card fraud have also changed.

For instance, when “Chip and Pin” technology was introduced, fraudulent transactions began to move more online.

As fraudulent behavior adapted, the performance of a model that had been developed before this technology would suddenly begin to suffer, and model predictions would be less accurate.

##### Data drift

  

**Data drift** refers to any change that has occurred to the data being fed to your model for prediction as compared to the data that was used for training.

Data drift can occur for a number of reasons:

- The input data schema changes at the source (for example, fields are added or deleted upstream).
- Feature distributions change over time (for example, a hospital might start to see more younger adults because a ski resort opened nearby).
- The meaning of the data changes even if the structure/schema hasn’t (for example, whether a patient is considered “overweight” may change over time).
- Software updates could introduce new bugs.
- The business scenario changes and creates a new product label previously not available in the training data.

  

Extract-Transform Load (ETL) pipelines for building, training, and predicting with ML models can be brittle and opaque, and any of these changes would have drastic effects on the performance of your model.

  

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996610-dt-content-rid-18302_1/xid-18302_1)

  

Take five minutes to think of a situation where you are designing an AI system that involves training a machine learning model using millions of records for an email spam filter, you reach a point where performance is sufficient and acceptable to the business owner,, So you deploy using a micro-services architecture and have a stateless function as a microservice.

Think in terms of concept and data drifts. What can go worng in six months? or one year?

Share with the class

#### **Solution**

  

Model deployment is a continuous process, and to solve for concept drift or data drift, it is necessary to update your training dataset and retrain your model with fresh data to improve predictions.

The most direct way to identify model deterioration is to continuously monitor your model’s predictive performance over time, and assess that performance with the same evaluation metrics you used during development. This kind of continuous model evaluation and monitoring is how we determine whether the model, or any changes we’ve made to the model, are working as they should.

Well, there are two things we need to look at:

**1- Additional data should be collected**

**Continuous evaluation** of this kind requires access to the:

1. **Raw prediction request data**
2. **The predictions the model generated**
3. **The ground truth (What really happened)**

All in the same place. The ground truth might be tricky and take time to collect.

For example, if the model is predicting whether a customer will renew a contract with a mobile operator in six months' time. Then one day, after six months, we need to see if the customer actually renewed or no longer exists in the operational database.

**2- Agree on a set of Metrics**

This happens through brainstorming sessions with the business owners and data scientists who trained the model. The purpose is to:

1. Anticipate any future data drift changes.
2. Anticipate any future concept drift changes.

This is not an easy task to do,  but examining the feature space is a starting point.

  

![Image generated by AI: Brain storming session](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996610-dt-content-rid-23230993_1/xid-23230993_1)

#### **Image generated by AI: Brainstorming session**

  

The metrics would be monitored against the agreed thresholds. If they are reached, then the system would initiate **triggers**, which might send alerts or automatically re-train the model.

We will cover more on this in future courses.

---

#### Why is it important from your end as an AI software designer?

  

In your architecture design, you would need to provision for components that address the collection of the production data and design components that address the triggers. This design pattern comes in handy.

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996610-dt-content-rid-40901_1/xid-40901_1)

  

- Chapter 5 "Machine Learning Design Patterns" by Valliappa Lakshmanan, Sara Robinson, and Michael Munn published by O'Reilly.
- Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung. 2003. The Google file system. _SIGOPS Oper. Syst. Rev_. 37, 5 (October 2003), 29-43. [https://dl.acm.org/doi/10.1145/1165389.945450](https://dl.acm.org/doi/10.1145/1165389.945450)
#### Design pattern "Batch Serving"

  

The Batch Serving design pattern uses software infrastructure commonly used for distributed data processing to carry out inference on a large number of instances all at once.

##### **Motivation:**

Predictions need to be carried out asynchronously over large volumes of data (contrary to predictions for small, individual requests), e.g., generating personalized playlists every week. This is only applicable if there is no need for (near-)real-time predictions.

As discussed in the previous topic, the serving framework is architected to process an individual request **synchronously and as quickly as possible.** The serving infrastructure is usually designed as a **microservice that offloads the heavy computation.**

_But wait, there are circumstances where predictions need to be carried out_ **_asynchronously_** _over_ **_large volumes of data_**

Let us look at some examples:

**Example 1:**

Determining whether to reorder a stock-keeping unit (SKU) might be an operation that is carried out hourly, not every time the SKU is bought at the cash register.

**Example 2:**

Music services might create personalized daily playlists for every one of their users and push them out to those users. The personalized playlist is not created on demand in response to every interaction that the user makes with the music software.

**The ML model needs to make predictions for millions of instances at a time, not one instance at a time.**

Attempting to take a software endpoint that is designed to handle one request at a time and sending it millions of SKUs or billions of users **will overwhelm the ML model.**

##### **Solution:**

Use a distributed data processing infrastructure to asynchronously carry out complex ML inference tasks on a large number of **computing nodes**. The individual predictions are aggregated back into a single result. The Batch Serving design pattern uses a **distributed data processing infrastructure**  (MapReduce, Apache Spark, BigQuery, Apache Beam, and so on) to carry out ML inference on a **large number of instances** **asynchronously**.

_Don’t worry about the distributed data processing frameworks for now, we will cover these in a future course, "Big data tools for machine learning" COMP251, let us understand the concept for now._

If the requests are not **latency-sensitive**, it is more cost-effective to use a distributed data processing architecture to invoke machine learning models on millions of items. The reason is that invoking an ML model on millions of items is a **parallel processing problem.**

It is possible to take the million items, break them down into 1,000 groups of 1,000 items each, send each group of items to a machine, and then **combine the results**.

Wow, that would be cool :)

The result of the machine learning model on item number 2,000 is completely independent of the result of the machine learning model on item number 3,000, and so it is possible to work on and **conquer it**.

In order to understand how this pattern is implemented, we need to understand two concepts:

###### 1) Distributed data/file processing.

###### 2) Parallel processing.

  

Let us have a closer look at each:

##### **Distributed file/data processing**

  

Let us look at Hadoop:

Hadoop Distributed File System (HDFS): Designed as an open version of Google’s file system GFS, HDFS is a distributed, scalable file system with notions of redundancy built in.

1. The design is to build the distributed file system on top of many nodes, each containing a regular file system.
2. Designed to scale and hold petabytes of data.
3. Design assumptions:
4. Sequential reads should be fast in support of full data scanning.
5. The file system should communicate sufficiently the location of the data so that computation can be moved to the data rather than the other way around.
6. Node failure should be tolerated in software.
7. HDFS does not support random reads or writes to files, but does support appending to a file.

How does it work?

A file, for example, **Data_file** is divided (cut) into blocks (B1,B2,B3…Bx), each 128 MB by default.

Data is organized inside of HDFS as blocks, and those blocks are transparently replicated. 

Have a look at the diagram below:

![Image showing a distributed file system](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996609-dt-content-rid-23244707_1/xid-23244707_1)

  

  

  

Image prepared by: Mayy Habayeb

Similarly, many other frameworks and data stores have the same capabilities. For example, Google BigQuery, MongoDB...etc.

##### Parallel processing

  

Let us look at MapReduce:

The first distributed data processing model supported by Hadoop was MapReduce, a computing model championed by Google.

Parallel MapReduce is defined as the distributed processing model whereby a problem can be broken down into three phases:

1. A map phase.
2. A shuffle phase.
3. A reduction phase. 

MapReduce relies on the data locality characteristics of HDFS and the task/resource management of YARN to efficiently run this three-step computation.

Map phase:

Input data are processed in parallel across the cluster through a method that transforms raw data into keys and values.

Shuffle phase

The keys are then sorted and “shuffled” into buckets by common, like keys (i.e., all values with the same key are guaranteed to go to the same reducer).

Reducer phase

Process the values for every key, often storing the results either back on HDFS or some other persistent store.

Technically speaking, we are using all the CPUs and memories of the devices (Nodes) on the shared network to work simultaneously.

Each node is considered a worker, and once it finishes the job, it reports back to the main node, and the cluster manager releases the resources.

New frameworks have emerged, and you can consider the **Spark framework.**

![Spark logo](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996609-dt-content-rid-23244709_1/xid-23244709_1)

  

Also, some datastores like **Google BigQuery**, which is a distributed datastore, have built-in capabilities for parallel processing.

#### Lambda architecture

  

A production ML system that supports both online serving and batch serving is called a Lambda architecture—such a production ML system allows ML practitioners to trade off between latency **(via the Stateless Serving Function pattern)** and throughput **(via the Batch Serving pattern)**.

A Lambda architecture is supported by having separate systems for online serving and batch serving.

**Example:**

Let us look at Google Cloud

- The online serving infrastructure is provided by Cloud AI Platform Predictions, and the batch serving infrastructure is provided by BigQuery and Cloud Dataflow (Cloud AI Platform Predictions provides a convenient interface so that users don’t have to explicitly use Dataflow).
- It is possible to take a TensorFlow model and import it into BigQuery for batch serving.
- It is also possible to take a trained BigQuery ML model and export it as a TensorFlow SavedModel for online serving.
- This two-way compatibility enables users of Google Cloud to hit any point in the spectrum of latency–throughput trade-off.

---

#### **Why is it important from your end as an AI software designer?**

  

It is to consider the nature of predications, look at:

1. Size of the data
2. Latency

If the size is large in millions of records and predications are not sensitive to time, then consider a distributed data framework and use the batch serving pattern.

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996609-dt-content-rid-40901_1/xid-40901_1)

  

- Chapter 5 "Machine Learning Design Patterns" by Valliappa Lakshmanan, Sara Robinson, and Michael Munn published by O'Reilly.
- Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung. 2003. The Google file system. _SIGOPS Oper. Syst. Rev_. 37, 5 (October 2003), 29-43. [https://dl.acm.org/doi/10.1145/1165389.945450](https://dl.acm.org/doi/10.1145/1165389.945450)



#### Design pattern "Stateless Serving Function"

  

#### **Stateless Serving Function**

  

The Stateless Serving Function design pattern makes it possible for a production **ML system to synchronously handle** thousands to millions of prediction requests per second.

**Motivation:**

Serve thousands to millions of prediction requests per second.

**Solution:**

Design an ML system around a stateless function that captures the architecture and weights of a trained model

1) Export the model into a format that captures the mathematical core of the model and is programming language agnostic

2) In the production system, the formula consisting of the "forward" calculations of the model is restored as a stateless function

3) The stateless function is deployed into a framework that provides a REST endpoint

The production **ML system is designed around a stateless function** that captures the **Architecture and weights of a trained model.**

  

_So what is a stateless function???_

A stateless function is a function whose outputs are determined purely by its **inputs**.

Have a look below at these two classes:

**Stateless**

﻿class Stateless:
    def __init__(self):
        self.weight = 3
        self.bias = 15
    def __call__(self, x):
        return self.weight*x + self.bias
 

If we instantiate an instance, call it **a**  of this class,  of this class, and invoke it three times or more with the value 10, we will always get the same answer 45:

>>> a= Stateless() 

>>> print(a(10))  

45

>>> print(a(10))

45

>>> print(a(10))

45

>>> print(a(10))

**Stateful**

﻿class State:
    def __init__(self):
        self.counter = 0
    def __call__(self, x):
        self.counter += 1
        if self.counter % 2 == 0:
            return 3*x + 15
        else:
            return 3*x - 15
 

If we instantiate an instance, call it **a**  of this class, and invoke it three times or more with the value 10, we will always get alternating answers between 15 and 45:

>>> a=State()

>>> print(a(10))

15

>>> print(a(10))

45

>>> print(a(10))

15

>>> print(a(10))

45

A function that maintains a counter of the number of times it has been invoked and returns a different value depending on whether the counter is odd or even is an example of a function that is **stateful**, not **stateless.**

The counter in this case is the state of the function, and the output depends on both the input (x) and the state (counter). The state is typically maintained using class variables (as in our example) or using global variables.

**Because stateless components don’t have any state, they can be shared by multiple clients.**

- Servers typically create an instance pool of **stateless components** and use them to service client requests as they come in.
- **Stateful components** will need to represent **each client’s conversational state**.
- The life cycle of **stateless components** needs to be managed by **the server**. They need to be initialized on the first request and destroyed when the client terminates or times out. 

Because of these factors, **stateless components** are **highly scalable**, whereas **stateful components** are expensive and difficult to manage.

When designing enterprise applications, architects are careful to **minimize the number of stateful components**.

Web applications, for example, are often designed to work based on REST APIs, and these involve the transfer of state from the client to the server with each call.

##### Machine learning models

  

When we train machine learning models, we specify a lot of **hyperparameters** depending on the algorithm we choose. For example, hyperparameters could be:

- The learning rate
- The number of epochs
- The regularization parameter
- The type of loss
- The optimization algorithm
- The number of neurons and hidden layers (in case of neural networks and deep learning)
- The number of leaves (in case of a decision tree)
- ..................................................

All these are required for the training and tuning, but **once a model is trained**, we don’t need any of these hyperparameters for the **inference (predictions)**.

All we need are the **learned parameters** from the training data based on the algorithm.

Let us look at an example:

Assume we have one million records of patients’ data. Per patient, we collect the age, body temperature, and body mass index(BMI).

Have a look at the data on the left.

The last column is the output column, sometimes we call it the label column. This column indicates that the medical team has examined the patient and has come to a conclusion about whether the patient is sick or not.

Using this data, we would like to train a predictive model to predict if a new patient would likely be sick or not based on three inputs: (01) Patient age, patient body temperature, and patient body mass index (BMI).

We decided to build a logistic regression model, don't worry for now how logistic regression works as an algorithm, that will be covered in other AI courses.

Let us have a look at the figure below, which illustrates both the training and inference processes.

Remember, our focus is on deploying a resilient model.

  

![Patient data](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996608-dt-content-rid-23244727_1/xid-23244727_1)

  

![Training and inference processes](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996608-dt-content-rid-23244728_1/xid-23244728_1)

  

Images prepared by: Mayy Habayeb

###### Training process

Following the black arrows is the training process, which, in most frameworks such as Sklearn and TensorFlow, usually uses the **fit() method**.

The input for the training is the training data and the algorithm with the hyperparameter values.

The output of the training process is literally four numbers that the algorithm learns from the training data.

We call these **the coiffiecents** of the models and sometimes refer to them as the **learned weights**.

This ends up storing the learned model in the main memory of the computer.

###### Inference process

This starts by receiving requests from various clients, as per the diagram. Let us assume we receive two requests simultaneously, one from a user using a laptop and the other from a user using a mobile.

Following the grey arrows, each request is sent to the learned model, the parameters in the request and the learned weights are used to generate the probabilities of the patient being sick or not.

This happens using the **predict() method** in a sequential manner.

##### **Problems**

Looks beautiful, but there are problems:

1. We have to load the entire model into memory. This would be an issue if we are using embeddings, especially in deep learning.
2. The preceding architecture imposes limits on the latency that can be achieved because calls to the predict() method have to be sent one by one.
3. Even though the data scientist’s programming language of choice is Python, model inference is likely to be invoked by programs written by developers who prefer other languages, or on mobile platforms like Android or iOS that require different languages.
4. The model input and output that is most effective for training may not be user-friendly, for example, the output is probabilities. 

  

![Image generated by AI: Issues & Problems](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996608-dt-content-rid-23230987_1/xid-23230987_1)

  

Image generated by AI : Problems

##### Solution

  

Three steps:

1. **Export the model** into a format that captures the mathematical core of the model and is programming language agnostic.
2. In the production system, the formula consisting of the “forward” calculations of the model is restored as a **stateless function**.
3. The stateless function is deployed into a **framework that provides a REST endpoint**.

  

  

![Solution](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996608-dt-content-rid-23230988_1/xid-23230988_1)

  

  

Image generated by AI :Solutions

##### 1- Export the model

  

_So how do we export a model? And what does that mean??_

What it means is to create an object that **captures the mathematical** model with the **learned weights** that can be saved on a hard disk; this is called serialization.

The how depends on the programming language and framework you are using.

Assuming you are using Sklearn and Python, there are two libraries you might want to consider:

pickle

cloudpickle

Joblib

Check out this link for a comparison    [https://scikit-learn.org/stable/model_persistence.htm](https://scikit-learn.org/stable/model_persistence.htm)

Assuming you are using TensorFlow, you can use SaveModel.

##### 2- Stateless function

  

To build the stateless function, one must understand the function’s input/output, which we call the **model signature**. Some frameworks provide this functionality, like TensorFlow has a tool named **saved_model_cli** to examine the exported file signature.

In scikit-learn, models are typically saved and loaded using Python’s pickle or joblib modules. When a scikit-learn model is loaded, it's a Python object, and its attributes and methods can be inspected directly using standard Python introspection tools.

To understand the "signature" of a scikit-learn model, one would typically examine:

- **Input Expectations**:
- fit method: This method usually expects input features (e.g., X) and target variables (e.g., y). The expected data types and shapes are generally described in the documentation for the specific scikit-learn estimator.
- predict or transform methods: These methods expect input features (X) that match the format used during training.
- **Output Expectations**:
- predict method: Returns predictions (e.g., class labels for classification, continuous values for regression).
- predict_proba method: Returns probability estimates for classification.
- transform method: Returns transformed features.

Here is an example:

import joblib
from sklearn.linear_model import LogisticRegression
 
# Assume 'model.joblib' is a saved scikit-learn model
# model = LogisticRegression()
# model.fit(X_train, y_train)
# joblib.dump(model, 'model.joblib')
 
loaded_model = joblib.load('model.joblib')
 
# Inspect attributes
print(f"Model type: {type(loaded_model)}")
print(f"Model coefficients: {loaded_model.coef_}")
print(f"Model classes (for classification): {loaded_model.classes_}")
 
# Check expected methods
print(f"Has 'predict' method: {'predict' in dir(loaded_model)}")
print(f"Has 'fit' method: {'fit' in dir(loaded_model)}")

  

**To create a Stateless Prediction Function:** Define a function that loads the model and performs predictions. This function should not modify any global state and should only depend on its input parameters and the loaded model.

Assuming we have trained a logistic regression model on the Iris dataset and exported/saved it using joblib, here is a suggested stateless function:

    import joblib
    import numpy as np
 
 
    def predict_logistic_regression(input_data_array):
        """
        Predicts using a pre-trained Logistic Regression model.
 
 
        Args:
            input_data_array (np.ndarray): A 2D NumPy array of features
                                           for prediction. Each row is a sample.
 
 
        Returns:
            np.ndarray: Predicted class labels.
        """
        # Load the pre-trained model (ensure this path is accessible)
        model = joblib.load('logistic_regression_model.joblib')
 
 
        # Make predictions
        predictions = model.predict(input_data_array)
        return predictions
 
 
    # Example usage:
    # Assuming you have new data for prediction
    new_data = np.array([[5.1, 3.5, 1.4, 0.2], [6.7, 3.0, 5.2, 2.3]])
    predictions = predict_logistic_regression(new_data)
    print(predictions)

  

It is important to define the serving function as a global variable (**or a singleton class**) so that it isn’t reloaded in response to every request.

##### 3- Create a web endpoint

  

The code above can be put into:

**1- A web application**. For web applications, we can use web frameworks such as FASTAPI  and define the endpoint.

- Because web application frameworks are so widely used, there is a lot of tooling available to measure, monitor, and manage web applications.
- If we deploy the ML model to a web application framework, the model can be monitored and throttled using tools that **software reliability engineers (SREs),** IT administrators, and DevOps personnel are familiar with.
- They do not have to know anything about machine learning.

**OR**

**2- A serverless framework** such as Google App Engine, Heroku, AWS Lambda, Azure Functions, Google Cloud Functions, Cloud Run, and so on. What all these frameworks have in common is that they allow the developer to specify a function that needs to be executed.

- The frameworks take care of autoscaling the infrastructure so as to handle large numbers of prediction requests per second at low latency.
- Business development personnel know how to meter and monetize web applications using API gateways.
- They can carry over that knowledge and apply it to metering and monetizing machine learning models.

#### Architectural style

  

Recall in module #2, we covered the SOA and micro-services architecture styles for arranging components of a software.

Well, usually in the **stateless function** would be implemented as a **microservice** within a microservices architecture style, especially in cloud-based deployments. We will cover this in our "Cloud machine learning" course COMP 264.

##### _What if the model cannot be called over a network?_

###### **Prediction library**

  

Instead of deploying the **serving function as a microservice** that can be invoked via a REST API, it is possible to implement the prediction code as a **library function**.

**The library function** would load the exported model the first time it is called, invoke **model.predict()** with the provided input, and return the result.

Application developers who need to predict with the library can then **include the library i**n their applications.

A library function is a better alternative than a microservice if the model cannot be called over a network, either because of physical reasons (there is no network connectivity) or because of performance constraints.

The library function approach also places the **computational burden on the client**, and this might be preferable from a budgetary standpoint.

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996608-dt-content-rid-40901_1/xid-40901_1)

  

- Chapter 5 "Machine Learning Design Patterns" by Valliappa Lakshmanan, Sara Robinson, and Michael Munn published by O'Reilly.


#### Design patterns for resilient AI serving at scale

  

#### Deployment and production environments

  

The purpose of a **machine learning model** is to use it **to make inferences (predictions) on data** it hasn’t seen **during training**. 

The same applies to **Large language models (LLMs);** the purpose is to **generate** **new context** different from the **original large data on which it was trained**.

  

Once a model has been trained or an LLM is either fine-tuned, it is typically deployed into a **production environment** and used to make predictions or generate new context in response to incoming requests. 

Have a look at the figure below:

![AI system deployed in production enviroment](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996502-dt-content-rid-23244708_1/xid-23244708_1)

  

Image prepared: by Mayy Habayeb

**Requests** can come from a variety of sources, such as web-enabled applications from computers, laptops, or mobile devices, or even other application servers that might pass a batch file containing many requests.

The AI capability will have to respond to these requests, **Responses** that are either **predictions** or **new content** if using LLMs.

  

Software that is deployed into production environments is expected to be **resilient** and require little in the way of human intervention to keep it running. 

  

##### Problems and challenges

Problems and challenges have been identified that apply to most deployments that involve AI. Some common ones are listed below:

1. Scaling to thousands of user requests.
2. Handling occasional or periodic requests for millions to billions of predictions.
3. Detecting when a deployed model is no longer fit-for-purpose.

##### **Solutions**

**Three design patterns** have been introduced to address the above-mentioned problems.

 **Design pattern: Stateless Serving Function**

to address the scaling to thousands of user requests.

**Design pattern: Batch Serving**

to address handling occasional or periodic requests for millions to billions of predictions.

**Design Pattern: Continued Model Evaluation**

to address detecting when a deployed model is no longer **fit-for-purpose**.

![Image generated by AI: Software design pattern](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996502-dt-content-rid-23230874_1/xid-23230874_1)

Image generated by AI: Software design pattern

  

![Activity 1 anner](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996502-dt-content-rid-18302_1/xid-18302_1)

  

Recall, in week #1, we talked about design patterns

Check out the same website and try to see if the above patterns are mentioned [AI patterns](https://swe4ai.github.io/ai-patterns/)

Check the category type and share it with the class.

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996502-dt-content-rid-40901_1/xid-40901_1)

  

- Chapter 5 "Machine Learning Design Patterns" by Valliappa Lakshmanan, Sara Robinson, and Michael Munn published by O'Reilly.
#### **TensorFlow framework**

  

As we noticed in the previous topic in the **framework layer** contains all AI-related frameworks to accelerate the process of AI-enabled application development and deployment, including tensor computing with strong acceleration via GPUs; the automatic differentiation system, **pre-building AI algorithm libraries, such as Torch and TensorFlow; and pre-building AI models, such as neural networks (NNs).**

##### _So what is TensorFlow??_

  

Let us start by watching this short video:

  

  

  

**TensorFlow** is a powerful, open-source library that makes building machine learning and artificial intelligence models much easier. Think of it as a giant toolbox for creating programs that can learn from data. It is considered **an end-to-end framework for machine learning and deep learning.**

  

###### Key Facts at a Glance

  

- **Who made it?**                   The Google Brain team.
- **When was it released?**   2015.
- **What language is it for?** Primarily Python, but it also works with JavaScript, C++, and Java.
- **What's a "Tensor"?**            Don’t let the name scare you! A tensor is just a fancy word for a multidimensional array of numbers. It’s the standard way data is handled in neural networks.
- **What other similar frameworks?** There are many, but PyTorch is one.

#### _Why is TensorFlow So Popular?_

TensorFlow is popular among both developers and companies because it's  powerful and accessible.

It's a Complete Package: It’s not just a math library. TensorFlow provides tools for every step of the process:

- Data processing and cleaning
- Building and training models
- Visualizing results
- Deploying models to apps and websites

It's Extremely Portable:

- In the cloud on powerful **GPUs** and Google's custom **TPUs (Tensor Processing Units).**
- On the mobile phones or even on tiny microcontrollers with **TensorFlow Lite**.
- In web browsers with **TensorFlow.js.**

Major companies use TensorFlow for critical tasks:

- Medicine: Analyzing MRI images to detect diseases.
- Spotify: Recommending new music.
- PayPal: Detecting fraudulent transactions.
- It's also key for self-driving cars, speech recognition.

##### What is a Tensor?

  

In the context of computer science and machine learning, a tensor is simply a multidimensional array of numbers. Think of it as a container for data that can have different levels of complexity. So technically a **data structure**. The number of dimensions a tensor has is called its **rank**.

Tensors in deep learning are not just n-dimensional arrays; there’s also the implicit assumption that they can be **run on a GPU**.

All tensors are immutable like Python numbers and strings: you can never update the contents of a tensor, only create a new one.

Notice that in other fields like mathematics and physics, Tensors are called **objects** and they are not just a data structure: they also have a list of properties, like a specific product.

Have a look at the table below to get a feel of the rank

|Rank|What it is|Common Name|Example in TensorFlow|Visual|
|---|---|---|---|---|
|0|A single, simple value.|Scalar|temperature = 25.0|25.0|
|1|A list or vector of values.|Vector|vector = [1.0, 2.5, -3.2]|[ 🟥 🟩 🟦 ]|
|2|A table or grid of values (rows and columns).|Matrix|matrix = [[1, 2, 3], [4, 5, 6]]|[[ 🟥 🟥 ],<br><br>[ 🟩 🟩 ],<br><br>[ 🟦 🟦 ]]|
|3|A cube or stack of matrices.|3-Tensor|A single grayscale image: [height, width, color_channels]|A cube made of smaller grids.<br><br>  <br><br>![cube](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996617-dt-content-rid-23244518_1/xid-23244518_1)<br><br>  <br><br>Image generated by AI: Cube|
|n|You can keep adding dimensions!|n-Tensor|A batch of color images: [batch_size, height, width, color_channels]|Hard to draw!|

  

  

_So, how is it different from NumPy multidimensional arrays?_

Generally speaking, they are much faster than NumPy arrays.

  

##### Layer in TensorFlow

_What are Layers in TensorFlow?_

In TensorFlow (and specifically using its **high-level Keras API)**, a layer is a fundamental building block of a neural network. Each layer takes in data, performs a specific transformation on it, and outputs a new (hopefully) more useful representation.

Think of it like an assembly line in a factory:

- Raw Materials (Input Data) go into the first station.
- Work Station (Layer) performs a specific task (e.g., cutting, shaping, painting).
- Processed Materials (Output) are passed to the next station.
- The Final Product (Model's Prediction) comes out at the end.

![Image generated by AI: production factory](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996617-dt-content-rid-23244516_1/xid-23244516_1)

Image generated by AI: production factory

###### The Core Idea: Feature Extraction & Hierarchy

  

The magic of deep learning is that these layers build on each other, creating a hierarchy of features from simple to complex.

  

**Example: Recognizing a Cat in an Image**

1. Early Layers might learn to detect simple edges, corners, and blobs of color.
2. Middle Layers combine those edges to detect more complex shapes like circles (eyes), triangles (ears), and fur texture.
3. Final Layers combine those shapes to recognize a full nose, a whisker pattern, and finally, the concept of a "cat face."

![Image generated by AI: Cat face](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996617-dt-content-rid-23244517_1/xid-23244517_1)

Image generated by AI: Cat face

##### **Each layer specializes in finding a specific type of pattern in the data.**

  

TensorFlow’s **Keras API** provides many pre-built layers. Here are the most essential ones:

###### 1. The Dense Layer (or Fully Connected Layer)

- What it does: This is the most common layer. Every neuron in a Dense layer is connected to every neuron from the previous layer. It performs a classic operation: output = activation(dot(input, kernel) + bias)
- Analogy: A team of experts where each expert looks at _all_ the evidence from the previous stage to make their own judgment.
- Use Case: The workhorse layer for the final stages of most networks.
- Key Parameter: units (number of neurons in the layer), activation (e.g., 'relu', 'sigmoid').

###### 2. The Conv2D Layer (Convolutional Layer)

- What it does: The superstar layer for image processing. Instead of connecting to every input, it uses a small "filter" (or "kernel") that scans across the image (like a flashlight) to detect local patterns like edges and textures.
- Analogy: Using a magnifying glass to systematically scan a photograph for specific small patterns.
- Use Case: Essential for any task involving images (and also great for some audio and text tasks).
- Key Parameters: filters (number of different patterns to look for), kernel_size (size of the magnifying glass, e.g., 3x3).

###### 3. The MaxPooling2D Layer (Pooling Layer)

- What it does: Downsamples the data. It takes a small window (e.g., 2x2) and outputs only the maximum value from that window. This makes the network faster, more efficient, and helps it focus on the most important features, making it more robust to the exact position of an object.
- Analogy: Summarizing a detailed paragraph into a single key sentence. You lose some detail, but you keep the core meaning.
- Use Case: Almost always used after convolutional layers in image models.

###### 4. The Flatten Layer

- What it does: Takes a multi-dimensional tensor (e.g., a 2D grid from a Conv layer) and "flattens" it into a 1D vector. This is necessary to connect a Conv2D layer to a Dense layer.
- Analogy: Taking a stack of forms (a 3D pile) and placing them all in one long, single-file line (a 1D vector) to be processed one-by-one.
- Use Case: A bridge between convolutional and dense layers.

###### 5. The Dropout Layer

- What it does: A regularization technique. During training, it randomly "drops out" (sets to zero) a fraction of the input units. This prevents the network from becoming overly reliant on any one neuron and helps it generalize better to new data, reducing overfitting.
- Analogy: Studying for a test by using different combinations of your notes each time, instead of memorizing one perfect order. This forces you to understand the concepts better.
- Key Parameter: rate (e.g., 0.5 means a 50% chance to drop any given neuron during training).

###### 6. The Input Layer

- What it does: This layer specifies the shape of the input data. It's the starting point of your model. It doesn’t perform any computation; it’s just a placeholder.
- Use Case: Defining what kind of data your model expects (e.g., (28, 28) for a grayscale image, (100,) for a vector of 100 features).

Just if you are interested, you can learn more about Keras layers here: [Keras layers](https://www.tensorflow.org/guide/keras/sequential_model?_gl=1*o8dk42*_up*MQ..*_ga*MTQ0Nzk3MjYxMS4xNzU1NzA4NzUx*_ga_W0YLR4190T*czE3NTU3MDg3NTEkbzEkZzAkdDE3NTU3MDg3NTEkajYwJGwwJGgw)

---

#### **Why is it important from your end as an AI software designer?**

  

Well, knowing that these frameworks and libraries exist will help you:

- Designing the components of the framework layer

_Don’t worry too much, now we will be covering the area in more detail as we move on in the program. There is a dedicated course for neural networks, followed by a dedicated course for deep learning_ 😊

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996617-dt-content-rid-40901_1/xid-40901_1)

  

- TensorFlow.org: [https://www.tensorflow.org/](https://www.tensorflow.org/)
- Fireship: [TensorFlow in 100 seconds](https://www.youtube.com/watch?v=i8NETqtGHms)
#### The Technology Stack

  

_Let's start by asking what a_ **_technology stack_**_, aka_ **_tech stack_**_, is???_

A Tech stack is a set of software **tools,** [**programming languages**](https://codeinstitute.net/global/blog/what-is-a-programming-language/)**,** [**frameworks**](https://codeinstitute.net/global/blog/what-is-a-framework/)**, libraries, and other technologies** used to build a particular software application or system and run it. The tech stack determines the application’s **capabilities, performance, and how it’s built and maintained.** 

A Tech stack typically includes a set of components and layers:

##### Components

1. Front-end (client-side) components
2. Back-end (server-side) components
3. Databases

##### Layers

  

Have you ever been to a wedding? If so, there is usually a wedding cake with layers. Well, that is how group technologies. Below are some examples:

1. **Operating system:** This layer manages the hardware and services the software. Examples, Linux, Windows, OS 400…etc
2. **Server-side programming:** To handle business logic, data processing, and communications with databases. Examples: Java, Python, PHP, Cobol, Ruby, Node.js, etc.
3. **Web servers:** For handling web requests, for example, Apache HTTP server, Microsoft IIS
4. **Database:** This layer consists of selecting and configuring a database management system (DBMS) to store and manage the system’s data. Examples: MongoDB, Microsoft SQL Server, SQLite, Cassandra, BigQuery, …etc.
5. **Client-side programming:** This layer consists of frameworks, programming languages, and libraries used for building the user interface and client-side logic. Examples, HTML, CSS, JavaScript, Angular, React, etc.
6. **Deployment and Infrastructure:** This layer includes tools and technologies to host and manage the application in a production environment. Examples: Cloud platforms, containerization technologies, workflow management systems, etc.

![Image generated by AI: wedding cake](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-23244511_1/xid-23244511_1)

Image generated by AI: wedding cake

Over the years, Many  Tech stacks have been introduced in software engineering, for example:

###### LAMP stack

The [**LAMP stack**](https://aws.amazon.com/what-is/lamp-stack/) **is a popular tech stack for software development**. It consists of four main components: **Linux, Apache, MySQL, and PHP****.**

Linux is an open-source operating system that provides a stable and secure platform for development. Apache is a widely used web server that supports various programming languages and is known for its flexibility and scalability. MySQL is a robust and dependable database management system, allowing quick and efficient data retrieval. PHP is a server-side scripting language that is widely used for web development.

The LAMP stack is well-known for its simplicity, adaptability, and low cost. LAMP allows developers to create dynamic, interactive web apps that are simple to maintain and scale. It is an excellent choice for web developers who are just starting or working on small to medium-sized projects.

But there may be better options for **large-scale projects requiring high scalability and performance,** or for complex projects that necessitate specialised knowledge.

###### .NET stack

The [.NET stack](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet) is a powerful technology stack developed by Microsoft, widely **used for building secure, scalable, and high-performance web and desktop applications.**

It consists of several components: **ASP.NET Core (the framework for web apps), C# (the programming language), and Microsoft SQL Server (the database).** This stack integrates seamlessly with the Microsoft ecosystem, including Azure for cloud services, Visual Studio for development, and other enterprise tools.

  

![Image generated by AI: Technology stack](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-23244510_1/xid-23244510_1)

  

Image generated by AI: Technology stack

![Activity  banner](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-18302_1/xid-18302_1)

  

Take ten minutes and research the following technology stacks:

###### **MEAN stack**

###### **MERN stack**

  

Check  for the following:

1. What technologies are used?
2. What best use cases?

Share with the class.

**Important**

The tech stack you choose directly influences your development speed, application performance, cost, scalability, and ability to attract technical talent. A mismatched stack can lead to project delays, technical debt, and user dissatisfaction. Selecting the optimal stack ensures your project stays on budget and on track. Choosing the technology stack depends highly on many factors, but the most important to consider is:

1- The use case

2- The organization’s exsisting IT blueprint

---

#### **The AI Tech-Stack Model**

  

With the introduction of AI and lately the Gen AI, which we will cover in module #6.  Enterprises have implemented advanced artificial intelligence (AI) technologies to support business process automation (BPA), provide valuable data insights, and facilitate employee and customer engagement.

In 2023, ACM published an article related to the AI tech stack. You can download it from here:

The AI Tech-Stack Model_3568026.pdf

  

Developing and deploying new AI-enabled applications poses some management and technology challenges.

Management challenges include:

1. Identifying appropriate business use cases for AI-enabled applications,
2. Lack of expertise in applying advanced AI technologies.
3. Insufficient funding.

Technology challenges include:

1. Organizations continuously encounter obsolete, incumbent information technology (IT)/information systems (IS) facilities.
2. Difficulty and complexity in integrating new AI projects into existing IT/IS processes
3. Immature and underdeveloped AI infrastructure
4. Inadequate data quantity and poor-quality learning requirements.
5. Growing security problems/threats.
6. Inefficient data preprocessing assistance

##### Cloud providers and third-party - AI-as-a-service (AIaaS)

The introduction of AI-as-a-service, **AIaaS,** adds to the options and complexities of the AI technology stacks.

They have stepped up efforts as major players in the AI-as-a-service (AIaaS) race by integrating cloud services with **AI core components** (for example, enormous amounts of data, advanced learning algorithms, and powerful computing hardware).

Although AlaaS offerings allow companies to take advantage of AI **without investing massive resources from scratch,** numerous issues have emerged to hinder the development of desired AI systems. Here are a few:

1. Current AI offerings are recognized as a fully bundled package, offering less interoperability between different vendors and causing **vendor lock-in** and proprietary concerns.
2. The **tightly coupled components** of different layers limit the extension of new functionality and inhibit developers’ flexibility and adaptability when choosing suitable AI components for practical implementation.
3. When a **vendor bundles several AI offerings into one package**, reliability becomes questionable since it is challenging to define a transparent service-level agreement (SLA) for each AI offering.
4. Bundled AI offerings are perceived as tightly controlled systems that inhibit the open source community’s support and raise the lock-in cost, which **increases potential incompatibility and introduces future migration costs** among different vendors.

Don’t worry, we will address some of these concerns in our Cloud machine learning course.

##### The seven-layered AI tech-stack mode

  

To address these issues, the mixed integration method was used to integrate cloud stacks with AI core components to propose the **seven-layered AI tech-stack model.** The seven layers, from bottom to top, are AI infrastructure, AI platform, AI framework, AI algorithm, AI data pipeline, AI services, and AI solution.

The AI infrastructure layer is closest to the machine, while the AI solution layer is closest to the end user.

To define each specific layer in the AI tech-stack model, the following principles were adopted:

1. Categorize similar functions into the same layer to enable function changes within a layer without affecting other layers.
2. Create a boundary at a point where the service description can be concise and the number of interactions across boundaries is minimized.
3. Decompose layers for handling AI jobs that are manifestly unique in task description or skill requirements.
4. Develop a boundary at a point where industry solutions are available and have proven useful.

  

![Suggested AI stack with seven layers](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-23244665_1/xid-23244665_1)

Suggested AI stack with seven layers

1. **AI infrastructure layer.** This layer integrates all IaaS components;[23](https://cacm.acm.org/research/the-ai-tech-stack-model/#R23) accelerators, such as graphics processing units (GPUs), tensor processing units (TPUs), and field-programmable gate arrays (FPGAs); and additional services, such as monitoring, clustering, and billing tools, to provide the hardware infrastructure environment for essential computation, storage, and network communication required by AI-enabled applications.
2. **AI platform layer.** This layer integrates the PaaS components (for example, operating systems, programming-language execution environment, database, web server, and so on), MLOps, and an intelligent engagement platform (IEP) for performing complete AI-enabled application lifecycle management. Specifically, it coordinates model building, evaluation, and monitoring to ensure the execution of AI applications’ continuous integration (CI), continuous delivery (CD), and continuous testing (CT).
3. **AI framework layer.** This layer contains all AI-related frameworks to accelerate the process of AI-enabled application development and deployment, including tensor computing with strong acceleration via GPUs; the automatic differentiation system, pre-building AI algorithm libraries, such as Torch and TensorFlow; and pre-building AI models, such as neural networks (NNs).
4. **AI algorithm layer.** This layer provides many well-defined open source and/or self-customized sets of AI algorithms (for example, supervised, unsupervised, and reinforcement learning) to help perform problem-solving and decision-making tasks.
5. **AI data pipeline layer.** This layer includes data as a service (DaaS) and the DataOps platform, which integrates various data architectures to facilitate the end-to-end data lifecycle. This layer also provides data-preprocessing functionalities and feature-engineering capabilities for managing internal and external data sources, manipulating various stationary and nonstationary data types, and handling batched and real-time data access.
6. **AI service layer.** This layer contains many ready-to-use, general-purpose APIs for AI-enabled services, such as image processing and nature language processing (NLP). The API transfers either the information (for example, insights derived from ML technologies) or raw data (for instance, source data for deriving insights through ML technologies) that can be executed with existing IT applications and/or enterprise systems—for example, enterprise resource planning (ERP), customer relationship management (CRM), and supply-chain management (SCM)—to deliver solutions in the upper level.
7. **AI solution layer.** This layer contains AI-enabled solutions to address problems in a specific business domain. With the AI solution layer, business analysts help domain users deliver broad AI capabilities in different companies or industry domains.

The proposed AI tech-stack model allows companies to have more informed choices among layers, choose AIaaS and third-party vendors based on SLA and pricing options, and leverage open source solutions to maintain flexibility.

**Example:**

**A smart (AI enabled)  Customer Relationship Management system (CRM)**

companies can choose Amazon as the AI infrastructure provider; MLflow to get the open source MLOps offering in the AI platform layer; the open source framework (for instance, TensorFlow, Keras, and PyTorch) in the AI framework layer; some in-house, customized, pre-built algorithms in the AI algorithm layer; third-party Hopsworks solutions to get DataOps tools in the AI data pipeline layer; external NLP and recommendation APIs in the AI service layer; and some in-house smart CRM solutions extending from incumbent CRM with AI-enabled NLP and recommendation services in the AI solution layer.

  

**The proposed AI tech-stack model allows companies to have more informed choices among layers, choose AIaaS and third-party vendors based on SLA and pricing options, and leverage open source solutions to maintain flexibility.**

  

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-18303_1/xid-18303_1)

  

This activity is 15 minutes:

Download the article in the AI-Tech-stack model section. Read the Tourism case study pages (75-76).

Share with the class what caught your attention.

The AI landscape

A company in NewYork named FIRSTMARK has been tracking the AI LAndscape for the past few years.

Have a look and compare the below two diagrams that illustrate the lansdscape grouth between 2020 and 2024. An enormous growth is happening the filed.

##### AI Landscape 2020

  

![2020 AI Landscape](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-23244662_1/xid-23244662_1)

  

  

  

  

2020-Data-and-AI-Landscape-Matt-Turck-at-FirstMark-v1.pdf

  

##### **AI Landscape 2024**

  

![2024 AI Landscape](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-23244664_1/xid-23244664_1)

  

  

AI Landscape 2024.pdf

  

  

  

  

![](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996616-dt-content-rid-18304_1/xid-18304_1)

  

It is so difficult to read the 2024 Landscape.

Form in groups of four or five

Navigate to [2024 AI Landscape](https://mad.firstmark.com/card)

Group #1: Check the infrastructure card

Group #2: check the Analytics card

Group #3: Check the Machine Learning and AI card.

Group #4: Check the Applications Enterprise card.

Group #5: Check the Open-source Infrastructure card.

Group #6: Check the data sources and api card.

Note the following:

1. The subgroups in each card
2. Any software that interests the group
3. Where do you think this software falls in the AI tech stack?

Each group chooses a representative to present to the class.

---

#### **Why is it important from your end as an AI software designer?**

  

Well, knowing that these technologies exist will help you:

- Designing the deployment of the system
- Designing the ongoing operations once the system is deployed
- Designing scalable systems

_Don’t worry too much, now we will be covering this area in more detail as we move on in the course._ 😊
#### **The Pipeline workflow design pattern**

  

In the Workflow Pipeline design pattern, we address the problem of creating an **end-to-end** reproducible pipeline by **containerizing** and **orchestrating** the steps in our machine learning process.

The containerization might be done **explicitly** or using a **framework that simplifies the process**.

##### **Motivation:**

  

An individual data scientist may be able to run data preprocessing, training, and model deployment steps from end to end as per the figure below within a single script or notebook.

  

![Machine LEarning pipeline](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996498-dt-content-rid-23244685_1/xid-23244685_1)

  

The steps in a typical end-to-end ML workflow.

  

In a large ML project, many teams might be working on one project.

**For example:**

For developing a weather prediction model, there could be three teams as follows:

1. One team is working on collecting and validating the data and carrying out the preprocessing.
2. A second team might be working on trying out different algorithms/models, training, and evaluating.
3. A third team might be setting up the deployment environment.

Have a look at the image below to get a better picture of the setup:

![Thee machine learning teams](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996498-dt-content-rid-23244682_1/xid-23244682_1)

Image prepared by Mayy Habayeb

Now these teams could be in **different countries.**

**Also,** notice that they are using **different software packages** and different versions.

As each step in an ML process **becomes more complex**, and **more people within an organization want to contribute** to this code base, running these steps from a single script (single monolithic application) will not scale.

- To test a small feature in a monolithic app, we must run the entire program.
- Deploying a small bug fix for one piece of the program requires deploying the entire application, which can quickly become unwieldy.

When the **entire codebase** is inextricably linked, it becomes **difficult for individual developers** to debug errors and work independently on different parts of the application.

Remember in module #3, we covered the **microservices** architecture style.

Monolithic apps have been replaced in favor of a microservices architecture where individual pieces of business logic are built and deployed as **isolated (micro) packages** of code.  Sounds great.

With microservices, a large application is split into **smaller, more manageable parts** so that developers can build, debug, and deploy pieces of an application independently.

**Microservices** are great for scaling **ML workflows.**

But to scale, we need three things:

1. We need the teams to **work independently**, regardless of the development environment.
2. We need to **track the performance** for each step of the pipeline.
3. We need to **manage the output files** generated by each part of the process.

So that sums up the problem

##### Solution

  

The solution comes in two parts, as follows:

1. Containerized services
2. Orchestrarizition

##### 1- Containerized service

Containers guarantee that we’ll be able to run the same code in **different environments,** and that we’ll see consistent behavior between runs.

These individual **containerized steps** are then chained together to make a _pipeline_ that can be run with a REST API call.

Because pipeline steps run in containers, we can run them on a development laptop, with on-premises infrastructure, or with a hosted cloud service.

This pipeline workflow allows team members to build out pipeline steps **independently**.

Containers also provide a **reproducible** way to run an entire pipeline end to end, since they guarantee consistency among library dependency versions and runtime environments.

Additionally, because containerizing pipeline steps allows for **a separation of concerns**, individual steps can use different runtimes and language versions.

_So how do we containrize??_

We can use software packages, listed below, just a few :

1. **Docker:** Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called [**containers**](https://aws.amazon.com/containers/) that have everything the software needs to run, including libraries, system tools, code, and runtime. 
2. **Podman:** A daemonless container engine compatible with Docker commands, often favored for its rootless capabilities and security features.
3. **Buildah:** A tool specifically designed for building OCI-compatible container images, offering fine-grained control over the image build process.
4. **containerd:** A core container runtime that provides the minimal set of functionalities for managing container lifecycles, used by many higher-level container platforms.
5. **CRI-O:** A lightweight container runtime specifically for Kubernetes, implementing the Container Runtime Interface (CRI).
6. **runc:** The low-level standard container runtime, providing the execution environment for containers.
7. **Kaniko:** A tool for building container images in environments without a Docker daemon, often used in CI/CD pipelines.

##### 2- Orchestrating the steps

  

To create the **ML pipeline** of containerized steps, we need tools that allow for **orchestration**.

What we mean by orchestration is a group of functionalities:

1. Chaining the containerized steps.
2. Monitoring the execution
3. Managing the inputs/outputs between the containerized ML steps.
4. Carrying out logic and interfacing with the external components, such as the operating systems.
5. Scheduling.

There are many tools for creating pipelines with both **on-premise** and **cloud options** available.

Listed below are just a few:

1. Amazon SageMaker pipelines
2. TensorFlow Extended (TFX) still needs Apache Beam underneath
3. Kubeflow Pipelines (KFP)
4. MLflow
5. Apache Airflow 

_So how do they work??_

Well, they use the concept of a **directed acyclic graph (DAG).**

A DAG is a conceptual framework used to **represent workflows**, data pipelines, or computational processes. It consists of **nodes** (tasks, operations, or computations) and **directed edges** (dependencies between these tasks).

Because the pipeline is a DAG, we have the option of:

- Executing individual steps or running an entire pipeline from end to end.
- This also gives us logging and monitoring for each step of the pipeline across different runs, and allows for tracking artifacts from each step and pipeline execution in a centralized place.

---

#### **Why is it important from your end as an AI software designer?**

  

Well, knowing that these technologies exist will help you:

- Designing the deployment of the system
- Designing the ongoing operations once the system is deployed
- Designing scalable systems

_Don’t worry too much, now we will be covering this area in more detail as we move on in the course._ 😊

  

![References](https://luminate.centennialcollege.ca/bbcswebdav/pid-3996498-dt-content-rid-40901_1/xid-40901_1)

  

  

- Chapter 6 "Machine Learning Design Patterns" by Valliappa Lakshmanan, Sara Robinson, and Michael Munn published by O'Reilly.
5. Non-Functional Requirements

This section specifies the non-functional requirements for the AI-Driven Job Matching Platform. These requirements define the quality attributes and constraints that the system must satisfy to meet stakeholder expectations.

5.1. Performance Requirements 5.1.1. Response Time

|   |   |
|---|---|
|ID|Requirement|
|NFR-01.|The system SHALL provide page load times of less than 3 seconds for standard operations under normal load conditions.|
|NFR-02.|The system SHALL provide search results within 2 seconds for standard search queries.|
|NFR-03.|The system SHALL complete AI matching operations within 5 seconds for individual job-candidate matches.|
|NFR-04.|The system SHALL process batch operations (e.g., bulk candidate matching) within a timeframe proportional to the batch size, not exceeding 2 minutes for standard operations.|
|NFR-05.|The system SHALL maintain response time degradation of no more than 50% during peak load periods.|

5.1.2. Throughput

|   |   |
|---|---|
|ID|Requirement|
|NFR-06.|The system SHALL support at least 1,000 concurrent users during normal operations.|
|NFR-07.|The system SHALL support at least 5,000 concurrent users during peak periods.|
|NFR-08.|The system SHALL process at least 100 job applications per minute during peak periods.|
|NFR-09.|The system SHALL support at least 500 new job postings per day.|
|NFR-10.|The system SHALL support at least 1,000 new user registrations per day.|

5.1.3. Resource Utilization

|   |   |
|---|---|
|ID|Requirement|
|NFR-11.|The system SHALL operate within the allocated server resources, utilizing no more than 80% of CPU capacity during normal operations.|
|NFR-12.|The system SHALL utilize no more than 80% of available memory during normal operations.|
|NFR-13.|The system SHALL require no more than 5TB of storage for the first year of operation, with a growth plan for subsequent years.|
|NFR-14.|The system SHALL optimize database queries to minimize I/O operations and response times.|
|NFR-15.|The system SHALL implement caching mechanisms to reduce resource utilization for frequently accessed data.|

28

5.1.4. Scalability

|   |   |
|---|---|
|ID|Requirement|
|NFR-16.|The system SHALL be designed to scale horizontally by adding more server instances to handle increased load.|
|NFR-17.|The system SHALL be designed to scale vertically by utilizing additional resources on existing servers.|
|NFR-18.|The system SHALL support a minimum of 100,000 registered job seekers without performance degradation.|
|NFR-19.|The system SHALL support a minimum of 10,000 registered employers without performance degradation.|
|NFR-20.|The system SHALL support a minimum of 50,000 active job postings without performance degradation.|
|NFR-21.|The system SHALL be designed to accommodate a 100% annual growth in user base and transaction volume for at least the first three years of operation.|

5.2. Security Requirements

5.2.1. Authentication and Authorization

|   |   |
|---|---|
|ID|Requirement|
|NFR-22.|The system SHALL implement multi-factor authentication for administrative accounts and as an option for all users.|
|NFR-23.|The system SHALL enforce strong password policies, including minimum length, complexity, and regular password changes.|
|NFR-24.|The system SHALL implement role-based access control (RBAC) to restrict access to features and data based on user roles.|
|NFR-25.|The system SHALL maintain detailed access logs for all authentication and authorization events.|
|NFR-26.|The system SHALL automatically lock accounts after a specified number of failed login attempts.|
|NFR-27.|The system SHALL implement secure session management with appropriate timeout settings.|
|NFR-28.|The system SHALL support OAuth 2.0 and OpenID Connect for third-party authentication where applicable.|

5.2.2. Data Protection

|   |   |
|---|---|
|ID|Requirement|
|NFR-29.|The system SHALL encrypt all sensitive data at rest using industry-standard encryption algorithms (AES-256 or equivalent).|
|NFR-30.|The system SHALL encrypt all data in transit using TLS 1.3 or higher.|
|NFR-31.|The system SHALL implement data masking for sensitive information displayed in the user interface.|
|NFR-32.|The system SHALL implement secure key management practices for encryption keys.|
|NFR-33.|The system SHALL provide mechanisms for secure data deletion when required.|
|NFR-34.|The system SHALL implement database-level encryption for sensitive tables and columns.|

29

|   |   |
|---|---|
|NFR-35.|The system SHALL maintain separate environments for development, testing, and production with appropriate data isolation.|

5.2.3. Privacy and Compliance

|   |   |
|---|---|
|ID|Requirement|
|NFR-36.|The system SHALL comply with Palestinian data protection regulations and incorporate GDPR principles as best practice.|
|NFR-37.|The system SHALL provide mechanisms for users to view, export, and delete their personal data in accordance with data protection regulations.|
|NFR-38.|The system SHALL maintain audit trails of all data access and modifications for compliance purposes.|
|NFR-39.|The system SHALL implement data minimization principles, collecting only necessary information for system functionality.|
|NFR-40.|The system SHALL provide clear privacy notices and obtain appropriate consent for data collection and processing.|
|NFR-41.|The system SHALL implement data retention policies in compliance with legal requirements.|
|NFR-42.|The system SHALL support data protection impact assessments (DPIA) for high-risk processing activities.|

5.2.4. Security Monitoring and Incident Response

|   |   |
|---|---|
|ID|Requirement|
|NFR-43.|The system SHALL implement comprehensive logging of security-relevant events.|
|NFR-44.|The system SHALL provide real-time monitoring and alerting for security incidents.|
|NFR-45.|The system SHALL implement intrusion detection and prevention mechanisms.|
|NFR-46.|The system SHALL conduct regular security scans and vulnerability assessments.|
|NFR-47.|The system SHALL have a documented incident response plan for security breaches.|
|NFR-48.|The system SHALL implement rate limiting and other protections against denial-of-service attacks.|
|NFR-49.|The system SHALL provide mechanisms for security patch management and updates.|

5.3. Reliability and Availability 5.3.1. Availability

|   |   |
|---|---|
|ID|Requirement|
|NFR-50.|The system SHALL maintain 99.5% availability during standard operating hours (8:00 AM to 8:00 PM Palestine time, Sunday through Thursday).|
|NFR-51.|The system SHALL maintain 99.0% availability during non-standard hours.|
|NFR-52.|The system SHALL schedule maintenance windows during periods of lowest expected usage.|
|NFR-53.|The system SHALL provide advance notice of scheduled maintenance to all users.|

30

|   |   |
|---|---|
|NFR-54.|The system SHALL implement high availability architecture to minimize single points of failure.|

5.3.2. Fault Tolerance

|   |   |
|---|---|
|ID|Requirement|
|NFR-55.|The system SHALL continue to function with degraded performance in the event of component failures.|
|NFR-56.|The system SHALL implement database replication to prevent data loss in case of database failures.|
|NFR-57.|The system SHALL implement load balancing across multiple servers to distribute traffic and prevent overload.|
|NFR-58.|The system SHALL automatically recover from common failure scenarios without manual intervention.|
|NFR-59.|The system SHALL implement circuit breaker patterns for external service dependencies to prevent cascading failures.|

5.3.3. Disaster Recovery

|   |   |
|---|---|
|ID|Requirement|
|NFR-60.|The system SHALL maintain regular backups of all data, with full backups at least weekly and incremental backups daily.|
|NFR-61.|The system SHALL store backups in geographically separate locations from the primary system.|
|NFR-62.|The system SHALL define and document Recovery Time Objective (RTO) of 4 hours for critical functions and 24 hours for non-critical functions.|
|NFR-63.|The system SHALL define and document Recovery Point Objective (RPO) of 1 hour, meaning no more than 1 hour of data loss in a disaster scenario.|
|NFR-64.|The system SHALL have a documented and tested disaster recovery plan.|
|NFR-65.|The system SHALL conduct disaster recovery drills at least twice per year.|

5.3.4. Error Handling

|         |                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------- |
| ID      | Requirement                                                                                                |
| NFR-66. | The system SHALL provide meaningful error messages to users without exposing sensitive system information. |
| NFR-67. | The system SHALL log detailed error information for troubleshooting and monitoring.                        |
| NFR-68. | The system SHALL handle input validation errors gracefully, providing clear feedback to users.             |
| NFR-69. | The system SHALL implement appropriate retry mechanisms for transient errors.                              |
| NFR-70. | The system SHALL maintain system stability when encountering unexpected inputs or conditions               |
**Assignment #2 –** **Design and Prototype an AI application (RAG) system**

  

Due Date: End of week #10

Purpose:

The purpose of this Lab assignment is to: 

  

1. Design an AI application system that uses RAG for System Requirements Engineering.
    
2. Draw Architecture and Component-level diagrams.
    
3. Explain design decisions.
    
4. Articulate the trade-offs involved in system design.
    
5. Create a prototype
    

  

General Instructions:

Be sure to read the following general instructions carefully: 

  

6. The exercise of this assignment must be completed individually by all the students. 
    
7. Only provide the requested screenshots, and make sure to have a complete screenshot; partial screenshots will not earn any marks.
    
8. You will have to add all the analysis and diagrams, screenshots to the Analysis report.
    
9. You will have to provide a demonstration video for your solution and upload the video together with the solution on Luminate through the assignment link.
    
10.  In your 6 – 8 minute demonstration video, you should explain your solution clearly, going over:
    
    1. The diagrams explain each component and its interaction with other components.
        
    2. The design decisions and why you took them.
        
    3. The design patterns you followed and why you chose them.
        
    4. The main code blocks of the prototype and the purpose of each method, also demoing the execution of the code.
        
11. YouTube links and links to Google Drive or any other media are not acceptable; the actual recording file in MP4 must be submitted.
    
12. Any submission without an accompanying video will lose 70% of the grade.
    
13. Any submission without an accompanying Analysis report will lose 70% of the grade.
    

  

Assignment Pre-requisites:

1. Anaconda
    
2. Langchain
    
3. Langchain-community
    
4. langchain-mistralai
    
5. Pypdf
    
6. chromadb
    
7. Sentence_transformers
    
8. Mistralai
    
9. python-dotenv
    

  

You can install all the required libraries by opening an Anaconda Prompt and executing the following commands.

  

conda install conda-forge::langchain

conda install conda-forge::langchain-community

conda install conda-forge::langchain-mistralai

conda install conda-forge::chromadb

conda install conda-forge::sentence-transformers

conda install conda-forge::pypdf

conda install conda-forge::python-dotenv-with-cli

  

If you are not using anaconda

Then you can use the pip command as follows:

  

pip install langchain langchain-community langchain-mistralai chromadb sentence-transformers pypdf python-dotenv

  

**Assignment Exercise**

  

**Design an AI application system that uses RAG for System Requirements Engineering**

System requirements are often scattered across multiple textual sources such as standards, regulations, and past project documents. This fragmentation makes it difficult for engineers to search for and locate specific information efficiently. Retrieval-Augmented Generation (RAG) addresses this challenge by retrieving relevant content from these distributed sources and presenting it in a concise, context-aware manner.

It also enables engineers to interact with the requirements through a chatbot that searches these documents to provide answers to their questions.

In this exercise, you will design and prototype a robust system that assists human engineers in efficiently searching through a requirements document. The prototype performs query-based searches, where it matches user queries with information contained in the requirements documents and extracts the most relevant requirements for a new system.

  

Exercise requirements:

1. Design (30 marks)
    

Assume you are designing a chatbot, named **ReqMind,** that is meant to assist engineers in software engineering activities. Provide the following:

1. An architecture diagram for **ReqMind.**
    
2. A UML component diagram that shows,
    
    1. the loading pipeline, which has an ingestion component that deals with the source data, a data transformation component that deals with the embeddings, and a loading component that interfaces with the data store Chroma DB.
        
    2. The inference pipeline should have a component for the client (frontend).
        

(Hint: Please check the following link: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-component-diagram/ ) to understand the component diagram and use only Visio, which provides you with the necessary notation. Make sure the interface names appear on the diagram.

3. A list of interfaces with their types (Internal or external).
    
4. Explain each component role and the main functions, elaborating on each step in each component.
    
5. Explain your design decisions, think of trade-offs.
    
6. List the design patterns you used and why you used them. (Minimum one design pattern).
    

  

Prototype requirements:

Before beginning the exercise, please follow the steps provided in Module **Week 9- Lab#2** to procure your Access Token Key for MistralAI. Make sure to store both the LLM API key and LLM name in a .env file.

Write Python code to load environment variables from the .env file. Additionally, store the input PDF files in the /data folder.

1. The **first task** is to turn unstructured PDF text in the documents into structured **Document** objects so LangChain can process it. To implement this functionality, write code that performs the following steps.
    
    1. Scans the **data/** folder for .**pdf** files.
        
    2. Use **PyPDFLoader** to extract text from each page.
        
    3. Returns a list of **Document** objects, where each object contains page_content: the text on that page and metadata: file name, page number, etc.
        

  

2. The **second task** is to add logic to split the documents into smaller chunks because long documents are difficult for models to handle all at once. Write a piece of code that performs the following.
    
    1. Use RecursiveCharacterTextSplitter from langchain.text_splitter to break each document into smaller text pieces by setting the parameters: chunk_size=1000 and chunk_overlap=100 to ensure context continuity between chunks.
        
    2. Print the number of chunks created and also the first 500 characters from the **first** chunk to preview the text boundaries. The code must create 12 chunks.
        

  

3. The **third Task** is to build the Vector Store. Follow the steps below to build the Vector store.
    
    1. Download the vector Embeddings using ‘SentenceTransformerEmbeddings’from langchain_community.embeddings library and set the model_name parameter to ll-MiniLM-L6-v2.
        
    2. To build the vector store, use the Chroma.from_documents() method from the Chroma vector store from langchain_community.vectorstores module. This method creates a searchable database of text embeddings that will later be used for retrieval. Pass the chunks generated in **Task #2** and the **embeddings** created in the previous step as parameters to this method.
        

You should also assign the parameter collection_name to **"rag_<studentid>"**. Additionally, to ensure the vector database is saved locally and can be reused in future runs, set the parameter persist_directory to **"./chroma_db"**.

Print a message “Vector store ready for retrieval” to indicate to the user that the Chroma Dbstore has been created.

4. The **fourth Task** is to implement the retrieval of relevant chunks from the database for a user query by following the steps below.
    
    1. Create an instance of the **MistralAI** object by instantiating the ChatMistralAI class from the langchain_mistralai module. When initializing this object, set the **api_key** parameter to the Mistral API key stored in your environment file, and specify the **model** parameter using the model’s name defined in that same file.
        

For example, you can use "mistral-large-latest" as the model name.

2. Use as_retriever method on the VectorDb object created in **Task 3(b)** and set search_kwargs={"k": 3}, which will retrieve the top 3 most relevant chunks for a given query.
    
3. Pass the MistralAI LLM object from step (a), the Retriever object from step (b) to RetrievalQA.from_chain_type() method from langchain.chains Module. Also, set the parameter chain_type="stuff" to "stuff" all context into the prompt, and the parameter return_source_documents to True to return the chunks used for retrieval.
    

Print a message “RAG chain successfully created” to indicate to the user that the Retriever with LLM is initialized.

5. The **final Task** is to put everything together into a chatbot application.
    
    1. Print the following message at the beginning of setting up the chatbot. “Starting firstname RAG Chatbot setup..” , where firstname is your first name.
        
    2. Print another message, “RAG Chatbot firstname ready! Type 'exit' to quit.” when the setup is complete.
        

Write Python code to enter an interactive loop. The loop first accepts a user query as input and terminates the loop if the user inputs’ exit' to quit.

3. Generate a context-aware answer by passing a query to the invoke method provided by the RetrievalQA object. The response contains both the answer and the source documents. Print the first 200 characters of all the source documents to show which document chunks were used as sources. Also display the bot-generated answer to the user.
    

An example output of the system for the query “_What should be the maximum response time for the system?_ ” is shown below.

Test your application by running **three queries**. Begin by submitting **two queries** that are directly related to the requirements described in your input requirements document. Record and analyze the chatbot’s responses in your **Analysis Report**.

Next, test the system’s behavior with **one unrelated query**—for example, _“Where is Centennial College?”_—to observe how the model handles questions outside the document’s scope. Document your observations in the **Analysis Report** as well.

  

Demonstration video (50 marks)

1. Record a demonstration video, explaining your design and going over the code in addition to executing the three required queries.
    

  

Naming and Submission Rules: 

1. You must name your submission according to the following rule: 
    

YourFullname_COMP248_assignmentnumber.Example: AdamPerjouski_COMP248_assignment1. Zip all your deliverables for the exercise into one file named according to the rule above. Please do not submit a .rar

2. Upload the submission file on Luminate using the Assignment link(s). 
    
3. In total, you should submit the following:
    
    1. One or more Python scripts (Python script means a .py file, not a notebook)
        
    2. One analysis report that contains your design, type your name at the top of the report.
        
    3. One demonstration video
        
    

  

  

**Rubric**

|   |   |   |   |   |   |
|---|---|---|---|---|---|
     
|Evaluation criteria|**Not acceptable**|**Below** **Average**|**Average**|**Competent**|**Excellent**|
||**0% - 24%**|**25%-49%**|**50-69%**|**70%-83%**|**84%-100%**|
|Design: Written analysis<br><br>Content (30%)|Missed all the key ideas; very shallow design.|Shows some thinking and reasoning, but most ideas are underdeveloped<br><br>in relation to the design, and design concepts are mostly not applied.|Indicates thinking and reasoning applied with original thought on a few ideas of the design.|Indicates original thinking and develops ideas with sufficient and firm evidence for most of the design elements.|Indicates synthesis of ideas, in-depth analysis, and evidence of original thought for all the design elements.<br><br>All required design elements have been submitted and follow the design concepts.|
|Prototype (20%)|Nothing submitted|Prototype code submitted, but it does not follow the design.|Prototype code submitted, but it fails on some aspects of the design.|Working prototype with a few discrepancies from the design.|Working prototype code follows the design.|
|Demonstration<br><br>Video (50%)|Very weak, no mention of the Key design ideas.<br><br>Prototype execution not demonstrated.|Some parts of the code changes are presented. Execution of code partially demonstrated.|All code changes were presented, but without an explanation of why. Code demonstrated.|All code changes were presented with an explanation, exceeding the time<br><br>limit. Prototype code explained and executed.|A comprehensive view of all the design elements presented with a clear explanation, within the time limit. Prototype code explained and executed.|

  

  

**Demonstration Video Recording** 

Please record a short video (max 8 minutes) to explain/demonstrate your assignment solution. You may use the Windows 10 Game Bar to do the recording: 

1. Press the Windows key + G at the same time to open the Game Bar dialog. 

2. Check the "Yes, this is a game" checkbox to load the Game Bar.  

3. Click on the Start Recording button (or Win + Alt + R) to begin capturing the video. 

4. Stop the recording by clicking on the red recording bar that will be on the top right of the program window. 

(If it disappears on you, press Win + G again to bring the Game Bar back.) 

You’ll find your recorded video (MP4 file) under the Videos folder in a subfolder called Captures. 

Or you can use any other video recording package freely available.