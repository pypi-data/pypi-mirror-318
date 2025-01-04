#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* bvkrylov.c */
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

#include "slepcbv.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvmatarnoldi_ BVMATARNOLDI
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvmatarnoldi_ bvmatarnoldi
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvmatlanczos_ BVMATLANCZOS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvmatlanczos_ bvmatlanczos
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  bvmatarnoldi_(BV V,Mat A,Mat H,PetscInt *k,PetscInt *m,PetscReal *beta,PetscBool *breakdown, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(H);
CHKFORTRANNULLINTEGER(m);
CHKFORTRANNULLREAL(beta);
*ierr = BVMatArnoldi(
	(BV)PetscToPointer((V) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((H) ),*k,m,beta,breakdown);
}
SLEPC_EXTERN void  bvmatlanczos_(BV V,Mat A,Mat T,PetscInt *k,PetscInt *m,PetscReal *beta,PetscBool *breakdown, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(T);
CHKFORTRANNULLINTEGER(m);
CHKFORTRANNULLREAL(beta);
*ierr = BVMatLanczos(
	(BV)PetscToPointer((V) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((T) ),*k,m,beta,breakdown);
}
#if defined(__cplusplus)
}
#endif
