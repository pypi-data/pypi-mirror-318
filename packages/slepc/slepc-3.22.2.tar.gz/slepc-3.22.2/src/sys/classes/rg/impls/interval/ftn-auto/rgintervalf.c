#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* rginterval.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcrg.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgintervalsetendpoints_ RGINTERVALSETENDPOINTS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgintervalsetendpoints_ rgintervalsetendpoints
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgintervalgetendpoints_ RGINTERVALGETENDPOINTS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgintervalgetendpoints_ rgintervalgetendpoints
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  rgintervalsetendpoints_(RG rg,PetscReal *a,PetscReal *b,PetscReal *c,PetscReal *d, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGIntervalSetEndpoints(
	(RG)PetscToPointer((rg) ),*a,*b,*c,*d);
}
SLEPC_EXTERN void  rgintervalgetendpoints_(RG rg,PetscReal *a,PetscReal *b,PetscReal *c,PetscReal *d, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLREAL(a);
CHKFORTRANNULLREAL(b);
CHKFORTRANNULLREAL(c);
CHKFORTRANNULLREAL(d);
*ierr = RGIntervalGetEndpoints(
	(RG)PetscToPointer((rg) ),a,b,c,d);
}
#if defined(__cplusplus)
}
#endif
