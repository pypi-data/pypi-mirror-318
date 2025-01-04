#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* dsops.c */
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

#include "slepcds.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetleadingdimension_ DSGETLEADINGDIMENSION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetleadingdimension_ dsgetleadingdimension
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetstate_ DSSETSTATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetstate_ dssetstate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetstate_ DSGETSTATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetstate_ dsgetstate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssetdimensions_ DSSETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssetdimensions_ dssetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetdimensions_ DSGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetdimensions_ dsgetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dstruncate_ DSTRUNCATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dstruncate_ dstruncate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsmatgetsize_ DSMATGETSIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsmatgetsize_ dsmatgetsize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsmatishermitian_ DSMATISHERMITIAN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsmatishermitian_ dsmatishermitian
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgettruncatesize_ DSGETTRUNCATESIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgettruncatesize_ dsgettruncatesize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetmat_ DSGETMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetmat_ dsgetmat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsrestoremat_ DSRESTOREMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsrestoremat_ dsrestoremat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsgetmatandcolumn_ DSGETMATANDCOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsgetmatandcolumn_ dsgetmatandcolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsrestorematandcolumn_ DSRESTOREMATANDCOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsrestorematandcolumn_ dsrestorematandcolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssolve_ DSSOLVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssolve_ dssolve
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssort_ DSSORT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssort_ dssort
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssortwithpermutation_ DSSORTWITHPERMUTATION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssortwithpermutation_ dssortwithpermutation
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dssynchronize_ DSSYNCHRONIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dssynchronize_ dssynchronize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsvectors_ DSVECTORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsvectors_ dsvectors
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dsupdateextrarow_ DSUPDATEEXTRAROW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dsupdateextrarow_ dsupdateextrarow
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dscond_ DSCOND
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dscond_ dscond
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dstranslateharmonic_ DSTRANSLATEHARMONIC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dstranslateharmonic_ dstranslateharmonic
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define dstranslaterks_ DSTRANSLATERKS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define dstranslaterks_ dstranslaterks
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  dsgetleadingdimension_(DS ds,PetscInt *ld, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(ld);
*ierr = DSGetLeadingDimension(
	(DS)PetscToPointer((ds) ),ld);
}
SLEPC_EXTERN void  dssetstate_(DS ds,DSStateType *state, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetState(
	(DS)PetscToPointer((ds) ),*state);
}
SLEPC_EXTERN void  dsgetstate_(DS ds,DSStateType *state, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSGetState(
	(DS)PetscToPointer((ds) ),state);
}
SLEPC_EXTERN void  dssetdimensions_(DS ds,PetscInt *n,PetscInt *l,PetscInt *k, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSSetDimensions(
	(DS)PetscToPointer((ds) ),*n,*l,*k);
}
SLEPC_EXTERN void  dsgetdimensions_(DS ds,PetscInt *n,PetscInt *l,PetscInt *k,PetscInt *t, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(n);
CHKFORTRANNULLINTEGER(l);
CHKFORTRANNULLINTEGER(k);
CHKFORTRANNULLINTEGER(t);
*ierr = DSGetDimensions(
	(DS)PetscToPointer((ds) ),n,l,k,t);
}
SLEPC_EXTERN void  dstruncate_(DS ds,PetscInt *n,PetscBool *trim, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSTruncate(
	(DS)PetscToPointer((ds) ),*n,*trim);
}
SLEPC_EXTERN void  dsmatgetsize_(DS ds,DSMatType *t,PetscInt *m,PetscInt *n, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(m);
CHKFORTRANNULLINTEGER(n);
*ierr = DSMatGetSize(
	(DS)PetscToPointer((ds) ),*t,m,n);
}
SLEPC_EXTERN void  dsmatishermitian_(DS ds,DSMatType *t,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSMatIsHermitian(
	(DS)PetscToPointer((ds) ),*t,flg);
}
SLEPC_EXTERN void  dsgettruncatesize_(DS ds,PetscInt *l,PetscInt *n,PetscInt *k, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(k);
*ierr = DSGetTruncateSize(
	(DS)PetscToPointer((ds) ),*l,*n,k);
}
SLEPC_EXTERN void  dsgetmat_(DS ds,DSMatType *m,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = DSGetMat(
	(DS)PetscToPointer((ds) ),*m,A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  dsrestoremat_(DS ds,DSMatType *m,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = DSRestoreMat(
	(DS)PetscToPointer((ds) ),*m,A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  dsgetmatandcolumn_(DS ds,DSMatType *m,PetscInt *col,Mat *A,Vec *v, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = DSGetMatAndColumn(
	(DS)PetscToPointer((ds) ),*m,*col,A,v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  dsrestorematandcolumn_(DS ds,DSMatType *m,PetscInt *col,Mat *A,Vec *v, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = DSRestoreMatAndColumn(
	(DS)PetscToPointer((ds) ),*m,*col,A,v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  dssolve_(DS ds,PetscScalar eigr[],PetscScalar eigi[], int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLSCALAR(eigr);
CHKFORTRANNULLSCALAR(eigi);
*ierr = DSSolve(
	(DS)PetscToPointer((ds) ),eigr,eigi);
}
SLEPC_EXTERN void  dssort_(DS ds,PetscScalar eigr[],PetscScalar eigi[],PetscScalar rr[],PetscScalar ri[],PetscInt *k, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLSCALAR(eigr);
CHKFORTRANNULLSCALAR(eigi);
CHKFORTRANNULLSCALAR(rr);
CHKFORTRANNULLSCALAR(ri);
CHKFORTRANNULLINTEGER(k);
*ierr = DSSort(
	(DS)PetscToPointer((ds) ),eigr,eigi,rr,ri,k);
}
SLEPC_EXTERN void  dssortwithpermutation_(DS ds,PetscInt perm[],PetscScalar eigr[],PetscScalar eigi[], int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(perm);
CHKFORTRANNULLSCALAR(eigr);
CHKFORTRANNULLSCALAR(eigi);
*ierr = DSSortWithPermutation(
	(DS)PetscToPointer((ds) ),perm,eigr,eigi);
}
SLEPC_EXTERN void  dssynchronize_(DS ds,PetscScalar eigr[],PetscScalar eigi[], int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLSCALAR(eigr);
CHKFORTRANNULLSCALAR(eigi);
*ierr = DSSynchronize(
	(DS)PetscToPointer((ds) ),eigr,eigi);
}
SLEPC_EXTERN void  dsvectors_(DS ds,DSMatType *mat,PetscInt *j,PetscReal *rnorm, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLINTEGER(j);
CHKFORTRANNULLREAL(rnorm);
*ierr = DSVectors(
	(DS)PetscToPointer((ds) ),*mat,j,rnorm);
}
SLEPC_EXTERN void  dsupdateextrarow_(DS ds, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSUpdateExtraRow(
	(DS)PetscToPointer((ds) ));
}
SLEPC_EXTERN void  dscond_(DS ds,PetscReal *cond, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLREAL(cond);
*ierr = DSCond(
	(DS)PetscToPointer((ds) ),cond);
}
SLEPC_EXTERN void  dstranslateharmonic_(DS ds,PetscScalar *tau,PetscReal *beta,PetscBool *recover,PetscScalar *g,PetscReal *gamma, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
CHKFORTRANNULLSCALAR(g);
CHKFORTRANNULLREAL(gamma);
*ierr = DSTranslateHarmonic(
	(DS)PetscToPointer((ds) ),*tau,*beta,*recover,g,gamma);
}
SLEPC_EXTERN void  dstranslaterks_(DS ds,PetscScalar *alpha, int *ierr)
{
CHKFORTRANNULLOBJECT(ds);
*ierr = DSTranslateRKS(
	(DS)PetscToPointer((ds) ),*alpha);
}
#if defined(__cplusplus)
}
#endif
