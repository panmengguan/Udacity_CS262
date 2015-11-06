
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '6EAFC46C319A94165BF42A1DE163AE51'
    
_lr_action_items = {'COMMA':([1,4,5,6,8,9,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,-2,-6,-7,39,-15,-8,-14,-9,-12,-11,-16,-13,-10,-17,-18,-19,]),'PLUS':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,12,-2,-6,12,-7,12,-15,12,12,12,12,12,-16,12,12,-17,-18,-19,]),'GT':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,16,-2,-6,16,-7,16,-15,16,-14,16,-12,-11,-16,-13,16,-17,-18,-19,]),'OROR':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,13,-2,-6,13,-7,13,-15,-8,-14,-9,-12,-11,-16,-13,-10,-17,-18,-19,]),'NOT':([0,2,3,11,12,13,14,15,16,17,18,19,20,21,22,39,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'RPAREN':([1,4,5,6,8,9,10,11,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,],[-3,-1,-4,-5,-2,-6,23,-21,-7,38,-20,-23,-15,-8,-14,-9,-12,-11,-16,-13,-10,-17,-18,-19,-22,]),'NUMBER':([0,2,3,11,12,13,14,15,16,17,18,19,20,21,22,39,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,4,5,6,7,8,9,23,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,0,-2,-6,-7,-15,-8,-14,-9,-12,-11,-16,-13,-10,-17,-18,-19,]),'LT':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,17,-2,-6,17,-7,17,-15,17,-14,17,-12,-11,-16,-13,17,-17,-18,-19,]),'STRING':([0,2,3,11,12,13,14,15,16,17,18,19,20,21,22,39,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]),'LPAREN':([0,2,3,4,11,12,13,14,15,16,17,18,19,20,21,22,39,],[3,3,3,11,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'MINUS':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,18,-2,-6,18,-7,18,-15,18,18,18,18,18,-16,18,18,-17,-18,-19,]),'EQUALEQUAL':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,20,-2,-6,20,-7,20,-15,20,-14,20,-12,-11,-16,-13,-10,-17,-18,-19,]),'TRUE':([0,2,3,11,12,13,14,15,16,17,18,19,20,21,22,39,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'LE':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,19,-2,-6,19,-7,19,-15,19,-14,19,-12,-11,-16,-13,19,-17,-18,-19,]),'TIMES':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,21,-2,-6,21,-7,21,21,21,21,21,21,21,21,21,21,-17,-18,-19,]),'FALSE':([0,2,3,11,12,13,14,15,16,17,18,19,20,21,22,39,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'DIVIDE':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,22,-2,-6,22,-7,22,22,22,22,22,22,22,22,22,22,-17,-18,-19,]),'ANDAND':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,15,-2,-6,15,-7,15,-15,15,-14,-9,-12,-11,-16,-13,-10,-17,-18,-19,]),'IDENTIFIER':([0,2,3,11,12,13,14,15,16,17,18,19,20,21,22,39,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'GE':([1,4,5,6,7,8,9,10,23,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-3,-1,-4,-5,14,-2,-6,14,-7,14,-15,14,-14,14,-12,-11,-16,-13,14,-17,-18,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'args':([11,39,],[25,40,]),'exp':([0,2,3,11,12,13,14,15,16,17,18,19,20,21,22,39,],[7,9,10,26,27,28,29,30,31,32,33,34,35,36,37,26,]),'optargs':([11,],[24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> IDENTIFIER','exp',1,'p_exp_identifier','ProblemSet4_JSExpressions.py',128),
  ('exp -> NUMBER','exp',1,'p_exp_number','ProblemSet4_JSExpressions.py',132),
  ('exp -> STRING','exp',1,'p_exp_string','ProblemSet4_JSExpressions.py',136),
  ('exp -> TRUE','exp',1,'p_exp_true','ProblemSet4_JSExpressions.py',140),
  ('exp -> FALSE','exp',1,'p_exp_false','ProblemSet4_JSExpressions.py',144),
  ('exp -> NOT exp','exp',2,'p_exp_not','ProblemSet4_JSExpressions.py',148),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp_parens','ProblemSet4_JSExpressions.py',152),
  ('exp -> exp OROR exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',171),
  ('exp -> exp ANDAND exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',172),
  ('exp -> exp EQUALEQUAL exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',173),
  ('exp -> exp LT exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',174),
  ('exp -> exp GT exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',175),
  ('exp -> exp LE exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',176),
  ('exp -> exp GE exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',177),
  ('exp -> exp PLUS exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',178),
  ('exp -> exp MINUS exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',179),
  ('exp -> exp TIMES exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',180),
  ('exp -> exp DIVIDE exp','exp',3,'p_binop','ProblemSet4_JSExpressions.py',181),
  ('exp -> IDENTIFIER LPAREN optargs RPAREN','exp',4,'p_call','ProblemSet4_JSExpressions.py',185),
  ('optargs -> args','optargs',1,'p_optargs','ProblemSet4_JSExpressions.py',189),
  ('optargs -> <empty>','optargs',0,'p_optargs_empty','ProblemSet4_JSExpressions.py',193),
  ('args -> exp COMMA args','args',3,'p_args','ProblemSet4_JSExpressions.py',197),
  ('args -> exp','args',1,'p_args_last','ProblemSet4_JSExpressions.py',201),
]