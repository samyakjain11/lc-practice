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
      let valBinding = ValueBinding(str,v) in
			Intermediate(valBinding :: env, exp_cps)
		| ExnMatch k ->
			(match v with IntVal a -> appExceptionHelper env k a
				| _ -> Failed)

let rec one_step_exp_cps_eval env exp_cps = 
	match exp_cps with
		| ConstCPS (k, c) -> app_cont_to_value env k (const_to_val c)
		| VarCPS (k, x) -> 
			(match lookup_value env x with
				| None -> Failed
				| Some v -> app_cont_to_value env k v)
    | MonOpAppCPS (k, operation, x, epsilon) ->
			(match lookup_value env x with 
				| None -> Failed
				| Some v -> 
					(match monOpApply operation v with 
						| Exn n -> appExceptionHelper env epsilon n
						| Value v' -> app_cont_to_value env k v'))
    | BinOpAppCPS(k, operation, x, y, epsilon) -> 
      (match (lookup_value env x, lookup_value env y) with 
      | (Some firstVal, Some secondVal) -> 
          (match binOpApply operation firstVal secondVal with
           | Exn n -> appExceptionHelper env epsilon n
           | Value v' -> app_cont_to_value env k v')
      | _ -> Failed)
    | AppCPS (k, f, x, epsilon) -> applyApp env k f x epsilon
    | IfCPS(e1, e2, e3) -> (match lookup_value env e1 with 
      | Some (BoolVal true) -> Intermediate (env, e2)  
      | Some (BoolVal false) -> Intermediate (env, e3)  
      | _ -> Failed )
		| FunCPS (k, x, ek, e, p) -> 
      let closureVal  = CPSClosureVal (x, ek, e, p, env) in
      app_cont_to_value env k closureVal
		| FixCPS (k, f, x, ek, e, p) ->
      let closureVal = (CPSRecClosureVal(f, x, ek, e, p, env)) in 
      app_cont_to_value env k closureVal

and applyApp env k f x epsilon = 
  match (lookup_value env f, lookup_value env x) with
  | (Some (CPSClosureVal (y, kk, ek, e, env')), Some v) -> 
      let valBinding = ValueBinding(y, v) in 
      let contBinding = ContBinding(kk, (k, env)) in 
      let exceptionBinding = ExnContBinding(ek, (epsilon, env)) in 
      let cpsEnvEntryList = (valBinding :: contBinding :: exceptionBinding :: env') in 
      Intermediate (cpsEnvEntryList, e)
  | (Some (CPSRecClosureVal(g, y, kk, ek, e, env')), Some v) -> 
      let valBinding = ValueBinding(y, v) in 
      let valBinding2 = ValueBinding(g, CPSRecClosureVal(g, y, kk, ek, e, env')) in 
      let contBinding = ContBinding(kk, (k, env)) in 
      let exceptionBinding = ExnContBinding(ek, (epsilon, env)) in 
      let cpsEnvEntryList = (valBinding :: valBinding2 :: contBinding :: exceptionBinding :: env') in 
      Intermediate (cpsEnvEntryList, e)
  | _ -> Failed
