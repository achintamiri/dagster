using Pandas
function filesmeth(r,r2)
    z = Pandas.concat([r,r2], axis=1)
    return z
end