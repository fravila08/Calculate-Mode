exports.calculateMode = (x) => {
    answer=[]
    compare=0
    let myObj={}
    x.forEach(function(i){myObj[i]=((myObj[i]||0)+1)})
    values=(Object.values(myObj))
    keys=(Object.keys(myObj))
    for (i=0;i<values.length;i++){
        if(values[i]>compare){
            compare= values[i]
        }
        else{
            continue
        }
    }
    for(j=0;j<values.length;j++){
        if(values[j]===compare){
            answer.push(keys[j])
        }
    }
    return(answer)
}


//calculateMode([4.5, 0, 0]) 
