#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* precond.c */
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

#include "slepcst.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stprecondsetksphasmat_ STPRECONDSETKSPHASMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stprecondsetksphasmat_ stprecondsetksphasmat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stprecondgetksphasmat_ STPRECONDGETKSPHASMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stprecondgetksphasmat_ stprecondgetksphasmat
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  stprecondsetksphasmat_(ST st,PetscBool *ksphasmat, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STPrecondSetKSPHasMat(
	(ST)PetscToPointer((st) ),*ksphasmat);
}
SLEPC_EXTERN void  stprecondgetksphasmat_(ST st,PetscBool *ksphasmat, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STPrecondGetKSPHasMat(
	(ST)PetscToPointer((st) ),ksphasmat);
}
#if defined(__cplusplus)
}
#endif
