F5 Control-Plane Security Onion Lab Guide
=========================================

Welcome to the **F5 Control-Plane Security Onion Lab Guide**.

This guide provides a structured, hands-on approach to securing the BIG-IP control plane
(TMUI, SSH, iControl REST/SOAP, and related services) using a layered **Outer → Middle → Core**
defense model.

The content is based on F5 security best practices, DevCentral guidance, and iHealth diagnostics,
and is intended for use in lab, training, and operational hardening environments.

---

Audience
--------

This guide is intended for:

* Network and security engineers
* Platform administrators
* Operations and hardening teams
* Training and lab participants

---

Learning Objectives
-------------------

After completing this guide, you will be able to:

* Understand the BIG-IP control-plane security model
* Apply layered security controls using the Security Onion framework
* Implement enterprise authentication and protocol hardening
* Validate configurations using F5 iHealth diagnostics
* Establish continuous monitoring and response procedures

---

Getting Started
---------------

.. toctree::
   :maxdepth: 1

   overview
   roadmap
   ihealth

---

Security Onion Layers
--------------------

These sections describe the conceptual security model and recommended controls at each layer.

.. toctree::
   :maxdepth: 1

   outer_layer
   middle_layer
   core_layer

---

Hands-On Labs
-------------

Follow these labs in order to implement and validate the Security Onion model.

.. toctree::
   :maxdepth: 1

   labs/index

---

Operational Resources
---------------------

Reference materials and operational guidance.

.. toctree::
   :maxdepth: 1

   checklist
   references

---

Navigation
----------

* :ref:`genindex`
* :ref:`search`
