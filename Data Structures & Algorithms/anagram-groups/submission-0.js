class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

    const ans = {};
    const offset = "a".charCodeAt(0);

    strs.forEach(str => {
        const freqs = new Array(26).fill(0);
        
        let i = str.length;
        while (i--) {
            freqs[str.charCodeAt(i)-offset]++;
        }
        const key = String(freqs);
        if (!ans[key]) {
            ans[key] = new Array();
        }
        ans[key].push(str);
    })
    
    return Object.values(ans);
    }
}
