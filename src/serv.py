o
    �I|a*  �                   @   sB   d dl Z d dlZd dlZd dlZdZdZdZdZdd� Ze�  dS )�    Nz[31mz[32mz[36mz[0mc                  C   s�   t �d�j} | dkr=ttd t d � ttd t d � ttd t d � t�d� t�d� t�d� t�	�  d S td� d S )	Nz1http://flyzero.000webhostapp.com/project/serv.php�1z[-]z= Error code: 000 The server is full. Please try again later. z; Error code: 000 The system cannot start without a server. z Server Status: Is full (>.<)i�  � )
�requests�get�text�print�R�W�time�sleep�sys�exit)r   � r   �serv.py�
serv_check   s   


r   )	r   r   �osr
   r   �G�Cr	   r   r   r   r   r   �<module>   s    
