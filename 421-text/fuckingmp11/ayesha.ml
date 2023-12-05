(* File: one_step_exp_cps_eval.ml *)

open Common;;

let rec keyValFinder givenList toFind = 
  match givenList with 
  | (Some key, value) :: kvs -> 
      if key = toFind then Some value else keyValFinder kvs toFind  
  | (None, defaultVal) :: kvs -> Some defaultVal 
  | [] -> None 

let rec appExceptionHelper env k a = 
  match k with EmptyExnContCPS -> UncaughtException a
    | ExnContVarCPS b -> contVarException env b a
    | UpdateExnContCPS (l, k') -> updateException env l k' a

and contVarException env b a = 
  match lookup_exn_cont env b with
  | None -> Failed
  | Some (k', env') -> appExceptionHelper env' k' a

and updateException env l k' a = 
  (match keyValFinder l a with
        | None -> appExceptionHelper
       env k' a 
        | Some v -> Intermediate (env, v))


let rec app_cont_to_value env k v = 
	match k with
		| External -> Final v 
		| ContVarCPS k ->
			(match lookup_cont env k with 
				| None -> Failed
				| Some (k', env') -> app_cont_to_value env' k' v)
		| FnContCPS (str, exp_cps) ->
			Intermediate(ValueBinding(str,v)::env, exp_cps)
		| ExnMatch k ->
			(match v with
				| IntVal a -> appExceptionHelper
       env k a
				| _ -> Failed)

let rec one_step_exp_cps_eval env exp_cps = 
	match exp_cps with
		| ConstCPS (k, c) -> app_cont_to_value env k (const_to_val c)
		| VarCPS (k, x) -> 
			(match lookup_value env x with
				| None -> Failed
				| Some v -> app_cont_to_value env k v)
    | MonOpAppCPS (k, mon_op, x, ke) -> apply_mon_op env k mon_op x ke
    | BinOpAppCPS(k, bin_op, x, y, ke) -> apply_bin_op env k bin_op x y ke
    | AppCPS (k, f, x, ke) -> apply_app_cps env k f x ke
    | IfCPS(b, e1, e2) -> apply_if_cps env b e1 e2
		| FunCPS (k, x, ek, e, p) -> app_cont_to_value env k (CPSClosureVal (x, ek, e, p, env))
		| FixCPS (k, f, x, ek, e, p) -> app_cont_to_value env k (CPSRecClosureVal(f, x, ek, e, p, env))

and apply_mon_op env k mon_op x ke = 
  match lookup_value env x with 
  | None -> Failed
  | Some v -> 
      (match monOpApply mon_op v with 
       | Exn n -> appExceptionHelper
       env ke n
       | Value v' -> app_cont_to_value env k v')

and apply_bin_op env k bin_op x y ke = 
  match (lookup_value env x, lookup_value env y) with 
  | (Some v1, Some v2) -> 
      (match binOpApply bin_op v1 v2 with
       | Exn n -> appExceptionHelper
       env ke n
       | Value v' -> app_cont_to_value env k v')
  | _ -> Failed

and apply_app_cps env k f x ke = 
  match (lookup_value env f, lookup_value env x) with
  | (Some (CPSClosureVal (y, kk, ek, e, env')), Some v) -> 
      Intermediate ((ValueBinding(y, v) :: ContBinding(kk, (k, env)) :: ExnContBinding(ek, (ke, env)) :: env'), e)
  | (Some (CPSRecClosureVal(g, y, kk, ek, e, env')), Some v) -> 
      Intermediate ((ValueBinding(y, v) :: ValueBinding(g, CPSRecClosureVal(g, y, kk, ek, e, env')) :: ContBinding(kk, (k, env)) :: ExnContBinding(ek, (ke, env)) :: env'), e)
  | _ -> Failed

and apply_if_cps env b e1 e2 = 
  match lookup_value env b with 
  | Some (BoolVal true) -> Intermediate (env, e1)  
  | Some (BoolVal false) -> Intermediate (env, e2)  
  | _ -> Failed 
