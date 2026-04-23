class Frac:
    """
    .. code-block:: lua
    ---Class in lua, btw
    ---@class Frac
    ---@field a integer
    ---@field b integer
    local Frac = {}
    Frac.__index = Frac
    """

    def __init__(self, a: int, b: int):
        """
        .. code-block:: lua
        ---__init__ in lua, btw
        ---@param a integer
        ---@param b integer
        ---@return integer
        function Frac:init(a,b)
            local obj = {
                a = a,
                b = b,
            }
            setmetatable(obj, self)
            return obj
        end
        """
        self.a = a
        self.b = b

    def gcd(self) -> int:
        """
        Greatest common Divisor

        Always return *postive int*, because of `abs(a)`

        .. code-block:: lua
        ---Greatest Common Divisor of two integers (a and b)
        ---Written in lua, btw
        ---@param a integer
        ---@param b integer
        ---@return integer
        function Frac:gcd()
            local a = self.a
            local b = self.b
            while true do
                local t = b
                b = a % b
                a = t
                if b == 0 then
                    break
                end
            end
            return math.abs(a)
        end

        return Frac
        """

        a = self.a
        b = self.b
        while True:
            t = b
            b = a % b
            a = t
            if b == 0:
                break
        return abs(a)
