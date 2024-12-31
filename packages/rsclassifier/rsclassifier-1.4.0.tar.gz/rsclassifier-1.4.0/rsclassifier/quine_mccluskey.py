'''
Terminology
-----------
Literal: A pair [b, p], where 'b' is either 0 or 1 (i.e., a bit), and 'p' is a string representing a variable.
- If b = 0, the literal corresponds to 'not p'.
- If b = 1, the literal corresponds to 'p'.

Term: A list of literals, representing a conjunction of literals (e.g., [p1, p2, not p3]).

This code aims to minimize a Disjunctive Normal Form (DNF) expression using prime implicants.
'''

def terms_match(term1 : list, term2 : list) -> int:
    """
    Compare two terms to see if they differ by exactly one literal (complement).
    - If two terms differ in more than one literal, they do not match.
    - If they match, the function returns the index where the literals complement each other.
    
    Args:
        term1 (list): The first term.
        term2 (list): The second term.
    
    Returns:
        int: The index where literals complement each other, or -1 if no match is found.
    """
    complement_found = -1  # Initialize to track if a complement (difference) is found.
    
    for i in range(len(term1)):
        if term1[i][1] != term2[i][1]:  # Literal names must match (p must be the same in both terms).
            return -1
        elif term1[i][0] != term2[i][0]:  # Check if literals are complements (e.g., p and not p).
            if complement_found != -1:  # More than one difference? Return -1 (no match).
                return -1
            else:
                complement_found = i  # Store the index of the complement.
    
    return complement_found  # Return the index of the complement, or -1 if no match.

def find_prime_implicants(terms : list) -> list:
    """
    Find all prime implicants by combining terms that differ by one literal (complements).
    
    Args:
        terms (list): A list of terms.
    
    Returns:
        list: A list of prime implicants.
    """
    # Sort the literals in each term by variable name (p) to enable term comparison.
    implicants = [sorted(term, key=lambda x: x[1]) for term in terms]
    prime_implicants = []  # List to store the prime implicants.

    while True:
        matches = [False] * len(implicants)  # Track which implicants have been combined.
        new_implicants = []  # Store new implicants generated by combining existing ones.

        # Compare each implicant with every other implicant.
        for i in range(len(implicants)):
            for j in range(i + 1, len(implicants)):
                result = terms_match(implicants[i], implicants[j])  # Check if they differ by one literal.
                if result != -1:
                    matches[i] = True  # Mark both implicants as "matched".
                    matches[j] = True
                    # Combine the two implicants by removing the complementing literal.
                    implicant = implicants[i][:result] + implicants[i][result + 1:]
                    if implicant not in new_implicants:
                        new_implicants.append(implicant)  # Add the new implicant if it's unique.

        # Any implicants that were not combined are prime implicants.
        for i in range(len(implicants)):
            if not matches[i]:
                prime_implicants.append(implicants[i])

        if len(new_implicants) == 0:  # If no new implicants were generated, we're done.
            break
        else:
            implicants = new_implicants  # Continue with the newly generated implicants.

    return prime_implicants

def issubset(implicant : list, term : list) -> bool:
    """
    Check if an implicant is a subset of a term.
    
    Args:
        implicant (list): An implicant (list of literals).
        term (list): A term.
    
    Returns:
        bool: True if the implicant is a subset of the term, otherwise False.
    """
    for literal in implicant:
        if literal not in term:
            return False
    return True

def find_sufficient_implicants(terms : list, implicants : list) -> list:
    """
    Find a minimal set of implicants that cover all the terms (i.e., sufficient implicants).
    
    Args:
        terms (list): A list of terms.
        implicants (list): A list of prime implicants.
    
    Returns:
        list: A list of sufficient prime implicants.
    """
    sufficient_implicants = []  # List to store the final sufficient implicants.
    local_terms = terms.copy()  # Copy terms to avoid modifying the original input.
    local_implicants = implicants.copy()  # Copy implicants for the same reason.

    # Repeat until all terms are covered.
    while len(local_terms) > 0:
        best_implicant = None
        best_implicant_covered_terms = []

        # Find the implicant that covers the most terms.
        for implicant in local_implicants:
            covered_terms = []
            for term in local_terms:
                if issubset(implicant, term):
                    covered_terms.append(term)

            if len(covered_terms) > len(best_implicant_covered_terms):
                best_implicant = implicant
                best_implicant_covered_terms = covered_terms

        sufficient_implicants.append(best_implicant)  # Add the best implicant to the final list.
        local_implicants.remove(best_implicant)  # Remove the selected implicant.
        
        # Remove the terms that were covered by the best implicant.
        for term in best_implicant_covered_terms:
            local_terms.remove(term)

    return sufficient_implicants

def minimize_dnf(terms : list) -> list:
    """
    Minimize a Disjunctive Normal Form (DNF) expression by finding sufficient implicants.
    
    Args:
        terms (list): A list of terms.
    
    Returns:
        list: A minimal set of implicants that cover the DNF expression.
    """
    return find_sufficient_implicants(terms, find_prime_implicants(terms))