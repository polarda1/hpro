a
    ��@a�  �                   @   s�   d dl Z d dlZd dlZd dlZe �d� ed� e�d� e �d� e �d� ee�d�d �Z	e j
�d�r�d	e	v r�e �d
� q�de	v r�e �d� q�ed� e j��  ne �d� e �d� e �d� dS )�    N�clearz  


Getting update ...g      �?zgit pull�P�   zuser.txtZ32zchmod +x h32 && ./h32Z64zchmod +x h64 && ./h64z


 aarch cannot identifiedzbpkg update && curl -L https://raw.githubusercontent.com/Hamzahash/uagents/main/user.txt > user.txtzVcurl -L https://raw.githubusercontent.com/Hamzahash/uagents/main/agent.txt >> user.txtzpython hop.py)�os�sys�timeZstruct�system�print�sleep�strZcalcsize�x�path�isfile�exit� r   r   �hop.py�<module>   s&   





