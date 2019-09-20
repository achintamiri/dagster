using JuMP
using SpineModel

function constraint_stor_cyclic(m::Model)
    @fetch stor_state = m.ext[:variables]
    constr_dict = m.ext[:constraints][:stor_cyclic] = Dict()
    stor_start = [first(stor_state_indices(storage=stor, commodity=c)) for (stor, c) in storage__commodity()]
    for (stor, c, t_first) in stor_start
        constr_dict[stor, c] = @constraint(
            m,
            stor_state[stor, c, t_first]
            ==
            stor_state[stor, c, time_slice()[end]]
        )
    end
end
input_url = "sqlite:///converted_inputs.sqlite"
output_url = "sqlite:///Output_db.sqlite"

m = run_spinemodel(input_url, output_url; cleanup=true, extend=m->constraint_stor_cyclic(m))
println("*** Active constraints: ***")
for key in keys(m.ext[:constraints])
    !isempty(m.ext[:constraints][key]) && println(key)
end
println("*** Active variables: ***")
for key in keys(m.ext[:variables])
    !isempty(m.ext[:variables][key]) && println(key)
end