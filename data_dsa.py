DSA_PROBLEMS_DATA = [
    {
        'topic': 'Arrays',
        'subtopic': 'Two Pointers / Hashing',
        'title': 'Two Sum',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/two-sum/',
        'gfg_url': 'https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/',
        'intuition': 'Store numbers and their indices in a hash map as you traverse. For each number x, check if (target - x) is already present in the map.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'python_code': '''def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []''',
        'cpp_code': '''vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> mp;
    for (int i = 0; i < nums.size(); ++i) {
        int diff = target - nums[i];
        if (mp.count(diff)) return {mp[diff], i};
        mp[nums[i]] = i;
    }
    return {};
}''',
        'java_code': '''public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int diff = target - nums[i];
        if (map.containsKey(diff)) return new int[]{map.get(diff), i};
        map.put(nums[i], i);
    }
    return new int[]{};
}''',
        'js_code': '''function twoSum(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i];
        if (map.has(diff)) return [map.get(diff), i];
        map.set(nums[i], i);
    }
    return [];
}'''
    },
    {
        'topic': 'Arrays',
        'subtopic': 'Kadane Algorithm',
        'title': 'Maximum Subarray (Kadane Algorithm)',
        'difficulty': 'Medium',
        'leetcode_url': 'https://leetcode.com/problems/maximum-subarray/',
        'gfg_url': 'https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/',
        'intuition': 'Maintain running sum. If running sum becomes negative, reset it to 0. Keep track of maximum sum encountered so far.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(1)',
        'python_code': '''def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for x in nums:
        curr_sum = max(x, curr_sum + x)
        max_sum = max(max_sum, curr_sum)
    return max_sum''',
        'cpp_code': '''int maxSubArray(vector<int>& nums) {
    int maxSum = nums[0], currSum = 0;
    for (int x : nums) {
        currSum = max(x, currSum + x);
        maxSum = max(maxSum, currSum);
    }
    return maxSum;
}''',
        'java_code': '''public int maxSubArray(int[] nums) {
    int maxSum = nums[0], currSum = 0;
    for (int x : nums) {
        currSum = Math.max(x, currSum + x);
        maxSum = Math.max(maxSum, currSum);
    }
    return maxSum;
}''',
        'js_code': '''function maxSubArray(nums) {
    let maxSum = nums[0], currSum = 0;
    for (let x of nums) {
        currSum = Math.max(x, currSum + x);
        maxSum = Math.max(maxSum, currSum);
    }
    return maxSum;
}'''
    },
    {
        'topic': 'Arrays',
        'subtopic': 'Prefix / Greedy',
        'title': 'Best Time to Buy and Sell Stock',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/',
        'gfg_url': 'https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/',
        'intuition': 'Track minimum purchase price seen so far. At each day, calculate current profit and update maximum profit.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(1)',
        'python_code': '''def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        if p < min_price: min_price = p
        elif p - min_price > max_profit: max_profit = p - min_price
    return max_profit''',
        'cpp_code': '''int maxProfit(vector<int>& prices) {
    int minPrice = INT_MAX, maxProfit = 0;
    for (int p : prices) {
        minPrice = min(minPrice, p);
        maxProfit = max(maxProfit, p - minPrice);
    }
    return maxProfit;
}''',
        'java_code': '''public int maxProfit(int[] prices) {
    int minPrice = Integer.MAX_VALUE, maxProfit = 0;
    for (int p : prices) {
        minPrice = Math.min(minPrice, p);
        maxProfit = Math.max(maxProfit, p - minPrice);
    }
    return maxProfit;
}''',
        'js_code': '''function maxProfit(prices) {
    let minPrice = Infinity, maxProfit = 0;
    for (let p of prices) {
        minPrice = Math.min(minPrice, p);
        maxProfit = Math.max(maxProfit, p - minPrice);
    }
    return maxProfit;
}'''
    },
    {
        'topic': 'Arrays',
        'subtopic': 'Sorting / Intervals',
        'title': 'Merge Intervals',
        'difficulty': 'Medium',
        'leetcode_url': 'https://leetcode.com/problems/merge-intervals/',
        'gfg_url': 'https://www.geeksforgeeks.org/merging-intervals/',
        'intuition': 'Sort intervals by start time. Iterate and merge with the previous interval if current interval start <= previous interval end.',
        'time_complexity': 'O(N log N)',
        'space_complexity': 'O(N)',
        'python_code': '''def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged''',
        'cpp_code': '''vector<vector<int>> merge(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> merged;
    for (auto& interval : intervals) {
        if (merged.empty() || merged.back()[1] < interval[0]) merged.push_back(interval);
        else merged.back()[1] = max(merged.back()[1], interval[1]);
    }
    return merged;
}''',
        'java_code': '''public int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
    List<int[]> merged = new ArrayList<>();
    for (int[] interval : intervals) {
        if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < interval[0]) merged.add(interval);
        else merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], interval[1]);
    }
    return merged.toArray(new int[merged.size()][]);
}''',
        'js_code': '''function merge(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    const merged = [];
    for (let interval of intervals) {
        if (merged.length === 0 || merged[merged.length - 1][1] < interval[0]) merged.push(interval);
        else merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
    }
    return merged;
}'''
    },
    {
        'topic': 'Strings',
        'subtopic': 'Sliding Window',
        'title': 'Longest Substring Without Repeating Characters',
        'difficulty': 'Medium',
        'leetcode_url': 'https://leetcode.com/problems/longest-substring-without-repeating-characters/',
        'gfg_url': 'https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/',
        'intuition': 'Use sliding window with two pointers left and right. Use a hash map to record the last seen index of characters.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(min(M, N))',
        'python_code': '''def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_len = 0
    for right, c in enumerate(s):
        if c in char_index and char_index[c] >= left:
            left = char_index[c] + 1
        char_index[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len''',
        'cpp_code': '''int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> mp;
    int left = 0, maxLen = 0;
    for (int right = 0; right < s.length(); ++right) {
        if (mp.count(s[right]) && mp[s[right]] >= left) left = mp[s[right]] + 1;
        mp[s[right]] = right;
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}''',
        'java_code': '''public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> map = new HashMap<>();
    int left = 0, maxLen = 0;
    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        if (map.containsKey(c) && map.get(c) >= left) left = map.get(c) + 1;
        map.put(c, right);
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}''',
        'js_code': '''function lengthOfLongestSubstring(s) {
    const map = new Map();
    let left = 0, maxLen = 0;
    for (let right = 0; right < s.length; right++) {
        if (map.has(s[right]) && map.get(s[right]) >= left) left = map.get(s[right]) + 1;
        map.set(s[right], right);
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}'''
    },
    {
        'topic': 'Linked Lists',
        'subtopic': 'Pointers Manipulation',
        'title': 'Reverse a Linked List',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/reverse-linked-list/',
        'gfg_url': 'https://www.geeksforgeeks.org/reverse-a-linked-list/',
        'intuition': 'Maintain prev, curr, and nxt pointers. At each step, direct curr.next to prev.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(1)',
        'python_code': '''def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev''',
        'cpp_code': '''ListNode* reverseList(ListNode* head) {
    ListNode *prev = nullptr, *curr = head;
    while (curr) {
        ListNode* nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}''',
        'java_code': '''public ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head;
    while (curr != null) {
        ListNode next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}''',
        'js_code': '''function reverseList(head) {
    let prev = null, curr = head;
    while (curr) {
        let next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}'''
    },
    {
        'topic': 'Linked Lists',
        'subtopic': 'Floyd Cycle Algorithm',
        'title': 'Detect Cycle in Linked List',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/linked-list-cycle/',
        'gfg_url': 'https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/',
        'intuition': 'Use slow (1 step) and fast (2 steps) pointers. If fast meets slow, a cycle exists.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(1)',
        'python_code': '''def hasCycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False''',
        'cpp_code': '''bool hasCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next; fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}''',
        'java_code': '''public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next; fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}''',
        'js_code': '''function hasCycle(head) {
    let slow = head, fast = head;
    while (fast && fast.next) {
        slow = slow.next; fast = fast.next.next;
        if (slow === fast) return true;
    }
    return false;
}'''
    },
    {
        'topic': 'Stacks & Queues',
        'subtopic': 'Matching / Stack',
        'title': 'Valid Parentheses',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/valid-parentheses/',
        'gfg_url': 'https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/',
        'intuition': 'Push opening brackets. For closing brackets, check if stack is non-empty and top matches.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'python_code': '''def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]: return False
        else: stack.append(char)
    return not stack''',
        'cpp_code': '''bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') st.push(c);
        else {
            if (st.empty()) return false;
            if (c == ')' && st.top() != '(') return false;
            if (c == '}' && st.top() != '{') return false;
            if (c == ']' && st.top() != '[') return false;
            st.pop();
        }
    }
    return st.empty();
}''',
        'java_code': '''public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
        if (c == '(' || c == '{' || c == '[') stack.push(c);
        else {
            if (stack.isEmpty()) return false;
            char top = stack.pop();
            if (c == ')' && top != '(') return false;
            if (c == '}' && top != '{') return false;
            if (c == ']' && top != '[') return false;
        }
    }
    return stack.isEmpty();
}''',
        'js_code': '''function isValid(s) {
    const stack = [];
    const map = { ')': '(', '}': '{', ']': '[' };
    for (let c of s) {
        if (map[c]) {
            if (stack.pop() !== map[c]) return false;
        } else {
            stack.push(c);
        }
    }
    return stack.length === 0;
}'''
    },
    {
        'topic': 'Trees & BST',
        'subtopic': 'DFS Recursion',
        'title': 'Maximum Depth of Binary Tree',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/maximum-depth-of-binary-tree/',
        'gfg_url': 'https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/',
        'intuition': 'Recursively calculate depth: 1 + max(depth(left), depth(right)). Base case returns 0 for null.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(H)',
        'python_code': '''def maxDepth(root) -> int:
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))''',
        'cpp_code': '''int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}''',
        'java_code': '''public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}''',
        'js_code': '''function maxDepth(root) {
    if (!root) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}'''
    },
    {
        'topic': 'Trees & BST',
        'subtopic': 'BFS Queue',
        'title': 'Binary Tree Level Order Traversal',
        'difficulty': 'Medium',
        'leetcode_url': 'https://leetcode.com/problems/binary-tree-level-order-traversal/',
        'gfg_url': 'https://www.geeksforgeeks.org/level-order-tree-traversal/',
        'intuition': 'Use BFS with a queue. Process level by level by noting queue length at start of each iteration.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(N)',
        'python_code': '''from collections import deque
def levelOrder(root) -> list[list[int]]:
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res''',
        'cpp_code': '''vector<vector<int>> levelOrder(TreeNode* root) {
    if (!root) return {};
    vector<vector<int>> res;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        while (sz--) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        res.push_back(level);
    }
    return res;
}''',
        'java_code': '''public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> res = new ArrayList<>();
    if (root == null) return res;
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);
    while (!q.isEmpty()) {
        int sz = q.size();
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < sz; i++) {
            TreeNode node = q.poll();
            level.add(node.val);
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
        res.add(level);
    }
    return res;
}''',
        'js_code': '''function levelOrder(root) {
    if (!root) return [];
    const res = [], q = [root];
    while (q.length) {
        const sz = q.length, level = [];
        for (let i = 0; i < sz; i++) {
            const node = q.shift();
            level.push(node.val);
            if (node.left) q.push(node.left);
            if (node.right) q.push(node.right);
        }
        res.push(level);
    }
    return res;
}'''
    },
    {
        'topic': 'Graphs',
        'subtopic': 'BFS / DFS Grid',
        'title': 'Number of Islands',
        'difficulty': 'Medium',
        'leetcode_url': 'https://leetcode.com/problems/number-of-islands/',
        'gfg_url': 'https://www.geeksforgeeks.org/find-number-of-islands/',
        'intuition': 'Iterate through grid. When encountering "1", increment island count and run BFS/DFS to sink all connected land to "0".',
        'time_complexity': 'O(M * N)',
        'space_complexity': 'O(M * N)',
        'python_code': '''def numIslands(grid: list[list[str]]) -> int:
    if not grid: return 0
    rows, cols, count = len(grid), len(grid[0]), 0
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1': return
        grid[r][c] = '0'
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1': count += 1; dfs(r, c)
    return count''',
        'cpp_code': '''int numIslands(vector<vector<char>>& grid) {
    int rows = grid.size(), cols = grid[0].size(), count = 0;
    auto dfs = [&](auto& self, int r, int c) -> void {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') return;
        grid[r][c] = '0';
        self(self, r+1, c); self(self, r-1, c); self(self, r, c+1); self(self, r, c-1);
    };
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == '1') { count++; dfs(dfs, r, c); }
        }
    }
    return count;
}''',
        'java_code': '''public int numIslands(char[][] grid) {
    int count = 0;
    for (int r = 0; r < grid.length; r++) {
        for (int c = 0; c < grid[0].length; c++) {
            if (grid[r][c] == '1') { count++; dfs(grid, r, c); }
        }
    }
    return count;
}
private void dfs(char[][] grid, int r, int c) {
    if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;
    grid[r][c] = '0';
    dfs(grid, r+1, c); dfs(grid, r-1, c); dfs(grid, r, c+1); dfs(grid, r, c-1);
}''',
        'js_code': '''function numIslands(grid) {
    let count = 0;
    const dfs = (r, c) => {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] !== '1') return;
        grid[r][c] = '0';
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1);
    };
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            if (grid[r][c] === '1') { count++; dfs(r, c); }
        }
    }
    return count;
}'''
    },
    {
        'topic': 'Dynamic Programming',
        'subtopic': '1D DP / Fibonacci',
        'title': 'Climbing Stairs',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/climbing-stairs/',
        'gfg_url': 'https://www.geeksforgeeks.org/count-ways-reach-nth-stair/',
        'intuition': 'Ways to reach step n is dp[n] = dp[n-1] + dp[n-2]. Space can be optimized to O(1) using two variables.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(1)',
        'python_code': '''def climbStairs(n: int) -> int:
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n + 1): a, b = b, a + b
    return b''',
        'cpp_code': '''int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; ++i) { int c = a + b; a = b; b = c; }
    return b;
}''',
        'java_code': '''public int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) { int c = a + b; a = b; b = c; }
    return b;
}''',
        'js_code': '''function climbStairs(n) {
    if (n <= 2) return n;
    let a = 1, b = 2;
    for (let i = 3; i <= n; i++) { let c = a + b; a = b; b = c; }
    return b;
}'''
    },
    {
        'topic': 'Dynamic Programming',
        'subtopic': 'Knapsack / Bottom-Up',
        'title': 'Coin Change',
        'difficulty': 'Medium',
        'leetcode_url': 'https://leetcode.com/problems/coin-change/',
        'gfg_url': 'https://www.geeksforgeeks.org/coin-change-dp-7/',
        'intuition': 'dp[a] = min coins for amount a. dp[a] = min(dp[a], 1 + dp[a - coin]). Base case dp[0] = 0.',
        'time_complexity': 'O(Amount * N)',
        'space_complexity': 'O(Amount)',
        'python_code': '''def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], 1 + dp[a - coin])
    return dp[amount] if dp[amount] != float('inf') else -1''',
        'cpp_code': '''int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    for (int coin : coins) {
        for (int a = coin; a <= amount; ++a) dp[a] = min(dp[a], 1 + dp[a - coin]);
    }
    return dp[amount] > amount ? -1 : dp[amount];
}''',
        'java_code': '''public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int coin : coins) {
        for (int a = coin; a <= amount; a++) dp[a] = Math.min(dp[a], 1 + dp[a - coin]);
    }
    return dp[amount] > amount ? -1 : dp[amount];
}''',
        'js_code': '''function coinChange(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    for (let coin of coins) {
        for (let a = coin; a <= amount; a++) dp[a] = Math.min(dp[a], 1 + dp[a - coin]);
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
}'''
    },
    {
        'topic': 'Backtracking & Recursion',
        'subtopic': 'Power Set',
        'title': 'Subsets (Power Set)',
        'difficulty': 'Medium',
        'leetcode_url': 'https://leetcode.com/problems/subsets/',
        'gfg_url': 'https://www.geeksforgeeks.org/power-set/',
        'intuition': 'Use backtracking. At each index, decide whether to include nums[i] or exclude it.',
        'time_complexity': 'O(2^N)',
        'space_complexity': 'O(N)',
        'python_code': '''def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    def backtrack(start, path):
        res.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res''',
        'cpp_code': '''vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res; vector<int> path;
    auto backtrack = [&](auto& self, int start) -> void {
        res.push_back(path);
        for (int i = start; i < nums.size(); ++i) {
            path.push_back(nums[i]); self(self, i + 1); path.pop_back();
        }
    };
    backtrack(backtrack, 0); return res;
}''',
        'java_code': '''public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();
    backtrack(res, new ArrayList<>(), nums, 0);
    return res;
}
private void backtrack(List<List<Integer>> res, List<Integer> path, int[] nums, int start) {
    res.add(new ArrayList<>(path));
    for (int i = start; i < nums.length; i++) {
        path.add(nums[i]); backtrack(res, path, nums, i + 1); path.remove(path.size() - 1);
    }
}''',
        'js_code': '''function subsets(nums) {
    const res = [];
    const backtrack = (start, path) => {
        res.push([...path]);
        for (let i = start; i < nums.length; i++) {
            path.push(nums[i]); backtrack(i + 1, path); path.pop();
        }
    };
    backtrack(0, []); return res;
}'''
    },
    {
        'topic': 'Bit Manipulation',
        'subtopic': 'XOR Trick',
        'title': 'Single Number',
        'difficulty': 'Easy',
        'leetcode_url': 'https://leetcode.com/problems/single-number/',
        'gfg_url': 'https://www.geeksforgeeks.org/find-element-appears-once-others-appear-twice/',
        'intuition': 'XOR of identical numbers is 0 (x ^ x = 0) and x ^ 0 = x. XORing all elements yields the unique element.',
        'time_complexity': 'O(N)',
        'space_complexity': 'O(1)',
        'python_code': '''def singleNumber(nums: list[int]) -> int:
    res = 0
    for x in nums: res ^= x
    return res''',
        'cpp_code': '''int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int x : nums) res ^= x;
    return res;
}''',
        'java_code': '''public int singleNumber(int[] nums) {
    int res = 0;
    for (int x : nums) res ^= x;
    return res;
}''',
        'js_code': '''function singleNumber(nums) {
    return nums.reduce((acc, curr) => acc ^ curr, 0);
}'''
    }
]
